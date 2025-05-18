import pyttsx3

if __name__ == '__main__':
    t_to_s = pyttsx3.init()
    print("Welcome to the text to speech converter")
    while True:
        word = input("Enter you words you want to speak:")
        if word.lower() == 'bye':
            t_to_s.say("Good bye!")
            t_to_s.runAndWait()
            break
        t_to_s.say(word)
        t_to_s.runAndWait()
