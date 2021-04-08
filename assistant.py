import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "spanish")

engine.say("Hola, esto es una prueba")
engine.runAndWait()