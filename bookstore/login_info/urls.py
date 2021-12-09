#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @time :2021/12/9 21:47
# @Author : liby
# @File: urls.py
# @Software : PyCharm

from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index')
]
