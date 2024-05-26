# import openai
import os
from utils import syntactic_check,repair

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from config import API_KEY

chat = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.2, api_key=API_KEY)


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a software testing assistant. " \
             "Please help me generate a whole JUnit test for the methods of the project under test. " \
             "I will provide the source code under test, including required dependencies to import. " \
             "I need you to create a whole unit test using JUnit 4, ensuring optimal branch coverage. " \
             "The test should include necessary imports for JUnit 4, compile without errors, " \
             "and use reflection to invoke private methods, preferably with necessary comments.",
        ),
        MessagesPlaceholder(variable_name="messages"),
    ]
)

chain = prompt | chat


messages = [
    HumanMessage(content="I'm giving you the source code."),
    AIMessage(content="The weather in New York today is sunny with a high of 75 degrees."),
]


number_to_word = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'forth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth'
}

# def generate_test():
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": "你好",
#             }
#         ],
#         model="gpt-3.5-turbo",
#     )
#     print(chat_completion.choices[0].message.content)


if __name__ == '__main__':
    project_path = r"projectsUT/Triangle"
    source_code_path = project_path + '/' + 'src/main/java/net/mooctest'
    # print(source_code_path)
    source_code_list = os.listdir(source_code_path)
    # generate_test()
    print(source_code_list[0])
    # 将所有源代码发送给GPT
    for i in range(len(source_code_list)):
        with open(source_code_path + '/' + source_code_list[i], "r") as f:
            source_code = f.read()
        content = f"The {number_to_word.get(i + 1)} java class is as follow: {source_code}"
        messages.append(HumanMessage(content=content))
        print(f'User: {content}')

        response = chain.invoke(
            {
                "messages": messages,
            }
        )
        test_code = response.content
        print(test_code)
        is_syntactic_correct = syntactic_check.is_syntactic_correct(test_code)
        print("Syntactic check result: {0}".format(is_syntactic_correct))
        if syntactic_check.is_syntactic_correct(test_code) is False:
            code_after_repair = repair.syntactic_repair(test_code)
        print(code_after_repair[1])


