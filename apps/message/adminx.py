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
    list_display = ['users', 'content', 'create_time']
    search_fields = ['users']
    list_filter = ['create_time']


xadmin.site.register(Message, MessageXadmin)
