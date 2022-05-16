#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Author:Mikigo
@Date  :2022/5/17 1:57
@Desc  :
"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]