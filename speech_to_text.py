import speech_recognition as sr

def listen_and_transcribe():
    #Create recognizer object
    recognizer = sr.Recognizer()

    #use microphones as source
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source,duration=2)

        print("Listening... Speak now!")
        audio = recognizer.listen(source)

    try:
        print("Recognizing speech...")
        #Use google's API to transcribe speech
        text = recognizer.recognize_google(audio)
        print("You said: ", text)

    except sr.UnknownValueError:
        print("Could not understand the audio. Please try again.")
    except sr.RequestError:
        print("API unavailable or network issue.")

if __name__ == "__main__":
    listen_and_transcribe()
