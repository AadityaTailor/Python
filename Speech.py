import speech_recognition as sr
Audio_file=("a.wav")

r=sr.Recognizer()

with sr.AudioFile(Audio_file) as source:
    audio=r.record(source)

try:
    print("Audio file contain: ",r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition could not understand audio")
except sr.RequestError:
    print("Couldn`t get the result from Google speech recognition")