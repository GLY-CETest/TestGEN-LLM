# TestGEN-LLM

## 简介
该项目为python项目，构建GPT对话，获得测试用例。

## 如何运行
1. 创建python环境，使用requirements.txt安装依赖库
2. 在config.py中设置API_KEY 
3. run gpt_test_generation.py，在命令行中可以打印gpt返回且经过修复的用例

## 项目结构
1. utils中目前包括语法检查和语法修复
2. projectsUT中为两个被测项目