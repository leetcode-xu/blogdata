#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/18 19:38
# @Author  : 徐纪茂
# @File    : adminx.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com

import xadmin
from .models import *


class TopicXadmin:
    list_display = ['title', 'read_num', 'content', 'image', 'blog_type', 'user']


class ReplyXadmin:
    list_display = ['topic', 'message', 'user1', 'user2', 'root']


class BlogTypeXadmin:
    list_display = ['type']


xadmin.site.register(Topic, TopicXadmin)
xadmin.site.register(Reply, ReplyXadmin)
xadmin.site.register(BlogType,BlogTypeXadmin)