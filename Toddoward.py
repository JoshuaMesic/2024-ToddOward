import speech_recognition as sr
import openai
import elevenlabs

# Set API keys
openai.api_key = "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"
elevenlabs.set_api_key("68e0afd04e31ca18a2dbd859ed22d81d")

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

        # Generate audio response using Eleven Labs
        audio = elevenlabs.generate(
            text=text,
            voice="Brian"  # or any voice of your choice
        )

        # Print and play the audio response
        print("\nAI:", text)
        elevenlabs.play(audio)

# Start conversation handling
handle_conversation()
