import os


def get_text_list(file_path):
    files = os.listdir(file_path)
    txt_lists = []
    for file in files:
        with open(os.path.join(file_path, file), 'r', encoding='UTF-8') as f:
            txt_lists.append(f.read())
    return txt_lists, files

# with open(r"D:\YGL\科研\博士\论文\ChatGPT用例生成\往年全国大赛试题\2021年全国大赛开发者测试省赛\GTree_1635641089780\result1635641086765\src\main\java\net\mooctest\Tree.java", 'r') as f:
#     content = f.read()
#     print(content)


if __name__ == '__main__':
    path = r'D:\YGL\科研\博士\论文\ChatGPT用例生成\往年全国大赛试题\2021年全国大赛开发者测试省赛\GTree_1635641089780\result1635641086765\src\main\java\net\mooctest'
    lists, fs = get_text_list(path)
    for i in range(len(lists)):
        print(lists[i])
        print(fs[i])

