import ollama
from gtts import gTTS
from dotenv import load_dotenv
import os
import platform

load_dotenv()

def analyze_text(text):
    response = ollama.generate(model=os.getenv('OLLAMA-MODEL'), prompt=text)
    return response['response']

def text_to_speech(text, filename="output.mp3"):
    # удаляем старый ответ
    try:
        os.remove(filename)
    except FileNotFoundError:
        print()
        # ничего не делаем..


    tts = gTTS(text=text, lang=os.getenv('LANGUAGE'))
    tts.save(filename)

    # определяем ос
    system_name = platform.system()
    if system_name == "Windows":
        os.system(f"start {filename}")
    elif system_name == "Darwin":  # мак дональд трамп
        os.system(f"afplay {filename}")
    else:  # линукс?
        os.system(f"mpg321 {filename}")

def main():
    while True:
        user_input = input("Введите ваш вопрос / Enter you question (или 'выход' для завершения / or 'exit' for ends work): ")
        if user_input.lower() in ["выход", "q", "quit", "exit"]:
            print("Пока :< / Bye :<")
            break

        analyzed_text = analyze_text(user_input)
        print("Ответ / Answer: " + analyzed_text)
        text_to_speech(analyzed_text)

if __name__ == "__main__":
    main()