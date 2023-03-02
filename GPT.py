import openai

openai.api_key = "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"


def ask_gpt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=100
    )
    return response.choices[0].text.strip()


while True:
    prompt = input("User: ")
    response = ask_gpt(prompt)
    print("ChatGPT: " + response)