import pyttsx3
import speech_recognition as sr
import re


def main():
    engine = pyttsx3.init()
    engine.setProperty("voice", "spanish")
    engine.say("Hola, esto es una prueba, ¿Cómo te llamas?")
    engine.runAndWait()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Puedes hablar...")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-MX")
    print(text)
    user_name = know_user_name(text, engine)


def know_user_name(text, engine):
    user_name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns:
        try:
            user_name = re.findall(pattern, text)
            print(user_name[0])
            engine.say("Hola {}, espero tengas un buen día".format(user_name[0]))
            engine.runAndWait()
            return user_name[0]
        except IndexError:
            print("Nombre no detectado")
            engine.say("Lo siento, no he escuchado tu nombre")
            engine.runAndWait()

if __name__ == "__main__":
    main()