# -*- coding: utf-8 -*-
#
# Time: 2024-01-17
# File: wechat_robot.py
# URL: https://github.com/CoderWanFeng/PyOfficeRobot/blob/main/README.md
# Description: 微信聊天机器人 智能回复
# venv/Lib/site-packages/PyOfficeRobot

# 安装库 pip install -i https://mirrors.aliyun.com/pypi/simple/ PyOfficeRobot -U

import PyOfficeRobot

# 智能聊天
# PyOfficeRobot.chat.chat_robot(who='wechat_name')

# 智能聊天（阿里模型）反应慢 不够智能 一眼看出是 AI
# 阿里云获取 API KEY: https://help.aliyun.com/zh/dashscope/developer-reference/activate-dashscope-and-create-an-api-key
PyOfficeRobot.chat.chat_ali(who='wechat_name', key="API_KEY")
