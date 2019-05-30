#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 10:10
# @Author  : 徐纪茂
# @File    : urls.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com
from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view()),
    path('addtopic/', AddTopic.as_view()),
    path('topicinfo/', TopicInfo.as_view()),
    path('reply/', ReplyAdd.as_view()),
    path('aixin/', AixinView.as_view()),
    path('list/', FenleiView.as_view()),
    path('ceshi/', CeShi.as_view()),
]