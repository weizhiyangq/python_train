# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 09:37:59 2018

@author: YWZQ
"""
'''
from chatterbot import ChatBot


# 构建ChatBot并指定Adapter
bot = ChatBot(
    'Default Response Example Bot',
    #storage_adapter='chatterbot.storage.StorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer'
)

# 手动给定一点语料用于训练
bot.train([
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

# 给定问题并取回结果
question = 'How do I make an omelette?'
print(question)
response = bot.get_response(question)
print(response)

print("\n")
question = 'how to make a chat bot?'
print(question)
response = bot.get_response(question)
print(response)

'''



'''
from chatterbot import ChatBot


bot = ChatBot(
    "yang_wei_zhi_Math & Time Bot",

    logic_adapters=[
    

        {
            'import_path': 'chatterbot.logic.MathematicalEvaluation'
        },
        {
            'import_path': 'chatterbot.logic.TimeLogicAdapter'
        },
        

        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.65,
            'default_response': 'I am sorry, but I do not understand.'
        }
    ],
    
    input_adapter="chatterbot.input.VariableInputTypeAdapter",
    output_adapter="chatterbot.output.OutputAdapter"
)

# 进行数学计算
question = "What is 4 + 9?"  #记得输入要标准，如不能写成4+9，中间的空格要有，否则识别不出，就会作为时间问题了
print(question)
response = bot.get_response(question)
print(response)

print("\n")

# 回答和时间相关的问题
question = "what's the time?"
print(question)
response = bot.get_response(question)
print(response)


# 进行数学计算
question = "What is sqrt 2?"
print(question)
response = bot.get_response(question)
print(response)

print("\n")
question = "how about sweather"

print(question)
response = bot.get_response(question)
print(response)
'''
#手动设置一些语料
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
 
 
Chinese_bot = ChatBot("Training demo")
Chinese_bot.set_trainer(ListTrainer)
Chinese_bot.train([
    '你好',
    '你好',
    '有什么能帮你的？',
    '想买数据科学的课程',
    '具体是数据科学哪块呢？'
    '机器学习',
])
 
# 测试一下
question = '你好ma'
print(question)
response = Chinese_bot.get_response(question)
print(response)

print("\n")

question = '请问哪里能数据科学的课程'
print(question)
response = Chinese_bot.get_response(question)
print(response)