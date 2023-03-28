import speech_recognition as sr

# Create a recognizer object
r = sr.Recognizer()

# Use the microphone as the audio source
with sr.Microphone() as source:

    # Set the threshold for ambient noise
    r.adjust_for_ambient_noise(source)

    # Ask the user to say something
    print("Say something!")
    audio = r.listen(source)

    # Recognize speech using Google Speech Recognition
    try:
        text = r.recognize_google(audio)
        print("You said: {}".format(text))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))