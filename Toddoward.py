import os
import speech_recognition as sr
import openai
from google.cloud import texttospeech

# Set OpenAI API key
openai.api_key = "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"

# Set Google Cloud credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "quiet-notch-416417-5bedaa33d410.json"

# Initialize Google Cloud Text-to-Speech client
client = texttospeech.TextToSpeechClient()

recognizer = sr.Recognizer()

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
                {"role": "system", "content": 'You are a highly skilled AI, answer the questions given within a maximum of 1000 characters.'},
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

        # Play the audio response
        import os
        os.system('start output.mp3')

# Start conversation handling
handle_conversation()
