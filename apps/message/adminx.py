#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 16:27
# @Author  : 徐纪茂
# @File    : adminx.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com
from message.models import Message
import xadmin


class MessageXadmin:
    list_display = ['user1','user2', 'content', 'create_time']
    search_fields = ['user1', 'user2']
    list_filter = ['create_time']


xadmin.site.register(Message, MessageXadmin)
