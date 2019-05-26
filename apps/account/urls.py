#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/16 14:37
# @Author  : 徐纪茂
# @File    : urls.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', Login.as_view()),
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('info/', InfoView.as_view()),
]