#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/17 11:07
# @Author  : 徐纪茂
# @File    : forms.py
# @Software: PyCharm
# @Email   : jimaoxu@163.com
from django import forms


class Verify_regis(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(max_length=16)
    email = forms.EmailField()
    url = forms.URLField()
    source_url = forms.URLField()