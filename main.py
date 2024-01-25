from openai import OpenAI

client = OpenAI()

messages = []

while True:
    try:
        prompt = input(">>> ")
        messages.append({"role": "user", "content": prompt})

        message = ""
        for chunk in client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                stream=True,
                ):
            content = chunk.choices[0].delta.content
            if content is not None:
                print(content, end="")
                message += content

        print()

        messages.append({"role": "assistant", "content": message})

    except KeyboardInterrupt:
        break


