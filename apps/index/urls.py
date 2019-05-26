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
    path('addtopic/', AddTopic.as_view())
]