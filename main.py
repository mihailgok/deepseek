from openai import OpenAI
from pathlib import Path
from mdtopdf import convertMD

KEY = "API_KEY"
SAVEPDF = False # Сохранять ли в ПДФ в папку pdf/

client = OpenAI(api_key=KEY, base_url="https://api.deepseek.com")

messages = []
i = 0

Path("answer/").mkdir(parents=True, exist_ok=True)

while True:
    userInput = input("Введите свой запрос:")

    if (userInput.strip() != ""):
        messages.append({"role": "user", "content": userInput})

        print("Ожидаем ответа..")

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages
        )

        messages.append(response.choices[0].message)

        i += 1
        with open(f'answer/answer{i}.md', 'w+') as file:
            file.write(response.choices[0].message.content)

        if SAVEPDF:
            Path("pdf/").mkdir(parents=True, exist_ok=True)

            convertMD(f"pdf/answer{i}", response.choices[0].message.content)

    else:
        print("Плохой запрос")
