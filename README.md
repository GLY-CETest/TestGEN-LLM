# TestGEN-LLM

## 简介
该项目为python项目，构建GPT对话，获得测试用例。

## 如何运行
1. 创建python环境，我当前python版本为3.9，激活python虚拟环境后，使用命令行，cd文件路径至当前项目的root目录下，使用requirements.txt安装依赖库

   ```pip install -r requirements.txt```
2. 在config.py中设置API_KEY 
   API_KEY为GPT的API KEY，首先需要有GPT账号，然后在官网申请API KEY，详见：
   https://platform.openai.com/account/api-keys
3. run gpt_test_generation.py，在命令行中可以打印gpt返回且经过修复的用例

## 项目结构
1. utils中目前包括语法检查和语法修复
2. projectsUT中为两个被测项目