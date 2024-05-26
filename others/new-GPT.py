from openai import OpenAI

# 设置 API key 和 API base URL
api_key = ""
base_url = "https://api.132999.xyz/v1"

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "你好\n你是谁？",
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion.choices[0].message.content)