# TestGEN-LLM

## 简介
该项目为python项目，构建GPT对话，获得测试用例。

This project is a Python project that builds GPT dialogues and obtains test cases.

## 如何运行
1. 创建python环境，我当前python版本为3.9，激活python虚拟环境后，使用命令行，cd文件路径至当前项目的root目录下，使用requirements.txt安装依赖库

   ```pip install -r requirements.txt```
   
1. Set up the Python environment. The recommend Python version is 3.9. 

activate the Python virtual environment

To create a virtual environment, decide upon a directory where you want to place it, 
and run the venv module as a script with the directory path:

python -m venv tutorial-env

This will create the tutorial-env directory if it doesn’t exist, and also create directories inside it containing a copy of the Python interpreter and various supporting files.

A common directory location for a virtual environment is .venv. This name keeps the directory typically hidden in your shell and thus out of the way while giving it a name that explains why the directory exists. It also prevents clashing with .env environment variable definition files that some tooling supports.

Once you’ve created a virtual environment, you may activate it.

On Windows, run:

tutorial-env\Scripts\activate

On Unix or MacOS, run:

source tutorial-env/bin/activate

After activating the Python virtual environment, 
use the command line to navigate to the root directory of the current project 
using `cd <file path>`. 
Install the dependency libraries using `requirements.txt`."

3. 在config.py中设置API_KEY 
   API_KEY为GPT的API KEY，首先需要有GPT账号，然后在官网申请API KEY，详见：
   https://platform.openai.com/account/api-keys

3. Set the API_KEY in config.py.
   The API_KEY is the GPT API key. First, you need to have a GPT account,
   then apply for an API key on the official website.
   
   For details, see:
   https://platform.openai.com/account/api-keys"
   
5. run gpt_test_generation.py，在命令行中可以打印gpt返回且经过修复的用例
   
5. Run
   
   gpt_test_generation.py.
   
   In the command line,
   you can print the test cases returned and fixed by GPT

## 项目结构
1. utils中目前包括语法检查和语法修复
2. projectsUT中为两个被测项目
