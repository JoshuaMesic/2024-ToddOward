import speech_recognition as sr
from gtts import gTTS
from openai import OpenAI
import os
import pyaudio


recognizer = sr.Recognizer()
client = OpenAI(api_key="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")

# used to listen to microphone and then create text


def speech_to_text():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return ""

# cookie cutter chat api needs work


def chat_gpt(messages):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant",
             "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    return response.choices[0].message['content']


def text_to_speech(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")


while True:
    input_text = speech_to_text()
    if input_text.lower() == 'exit':
        break
    response = chat_gpt(input_text)
    print("ChatGPT:", response)
    text_to_speech(response)
