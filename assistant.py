import re
from speak_n_listen import speak, listen


def main():
    saludo = "Hola, esto es una prueba, ¿Cómo te llamas?"
    speak(saludo)
    text = listen()
    print(text)
    user_name = know_user_name(text)


def know_user_name(text):
    user_name = None
    patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)", "^([A-Za-z]+)$"]
    for pattern in patterns: # TODO: Fix user name detection ---- ¿LIST OUT OF RANGE? ---- re might be the problem
        try:
            user_name = re.findall(pattern, text)
            print(user_name[0])
            speak("Hola {}, espero tengas un buen día".format(user_name[0]))
            return user_name[0]
        except IndexError:
            print("Nombre no detectado")
            speak("Lo siento, no he escuchado tu nombre")

if __name__ == "__main__":
    main()