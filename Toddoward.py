import os
import speech_recognition as sr
import openai
from google.cloud import texttospeech
import pygame
from gpiozero import Servo
import math
from time import sleep
import threading 

# Set OpenAI API key
openai.api_key = "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"

# Set Google Cloud credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "quiet-notch-416417-5bedaa33d410.json"

# Initialize Google Cloud Text-to-Speech client
client = texttospeech.TextToSpeechClient()

recognizer = sr.Recognizer()

# Initialize pygame mixer
pygame.mixer.init()

def recognize_speech():
    while True:
        try:
            with sr.Microphone() as mic:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                text = text.lower()
                print("Recognized:", text)
                return text
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
        except sr.RequestError as e:
            print("Could not request results from Google Web Speech API; {0}".format(e))

def handle_conversation():
    while True:
        # Get user input
        user_input = recognize_speech()

        # Send user input to OpenAI for response generation
        response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=[
                {"role": "system", "content": "You are Todd Howard, the Bethesda game developer. You love talking about various things such as Skyrim, Fallout and Morrowind. Have some variability in your responses and try to banter a lot. Make your responses very human and casual. Limit the responses to 500 characters."},
                {"role": "user", "content": user_input}
            ]
        )

        # Extract response from OpenAI
        text = response['choices'][0]['message']['content']

        # Print AI response
        print("\nAI:", text)

        # Generate audio response using Google Cloud Text-to-Speech API
        synthesis_input = texttospeech.SynthesisInput(text=text)
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",  # Specify desired language code
            name="en-US-Neural2-A",  # Specify desired voice model
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3  # MP3 audio format
        )
        response = client.synthesize_speech(
            input=synthesis_input, voice=voice, audio_config=audio_config
        )

        # Save the audio response to a file
        with open('output.mp3', 'wb') as out:
            out.write(response.audio_content)

        # Play the audio response using pygame
        pygame.mixer.music.load('output.mp3')
        pygame.mixer.music.play()

        # Wait for the audio to finish playing
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

        # Add a check to ignore input if it matches the AI response
        if user_input.lower() == text.lower():
            continue

# Start conversation handling in a separate thread
conversation_thread = threading.Thread(target=handle_conversation)
conversation_thread.start()

# Servo control code
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(12, min_pulse_width=0.5/1000,
              max_pulse_width=2.5/1000, pin_factory=factory)

while True:
    for i in range(0, 360):
        servo.value = math.sin(math.radians(i))
        sleep(0.01)
