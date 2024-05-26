import openai
from read import get_text_list
from tenacity import retry, stop_after_attempt, wait_random_exponential

openai.api_key = ""
messages = [{'role': 'system',
             'content': "Please help me generate a whole JUnit test for a focal method in a focal class. "
                        "I will provide the following information: "
                        "1. Required dependencies to import. "
                        "2. The focal class signature. "
                        "3. Source code of the focal method."
                        "I need you to create a whole unit test using JUnit 4, ensuring optimal branch coverage. "
                        "The test should include necessary imports for JUnit 4, compile without errors, "
                        "and use reflection to invoke private methods. "
                        "No additional explanations are required."}]


def chat_completion(content):
    messages.append({'role': 'user', 'content': content})


def give_prompt():
    pass


if __name__ == '__main__':
    # print(openai.Model.list())
    while True:
        content = input("User:")
        print("Input:{0}".format(content))
        messages.append({'role': 'user', "content": content})
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=1024
        )

        print(f'chatGPT: {completion}')
        print(f'Answer:{completion.choices[0].message.content}')
        # print(f'finish_reason: {completion.choices[0].finish_reason}')


