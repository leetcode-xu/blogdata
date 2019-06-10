#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 16:12
# @Author  : 徐纪茂
# @File    : urls.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com
from django.urls import path
from .views import *

urlpatterns = [
    path('gbook/', GbookView.as_view()),
]