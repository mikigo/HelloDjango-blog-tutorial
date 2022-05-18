#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Author:Mikigo
@Date  :2022/5/18 23:09
@Desc  :
"""

from django.urls import path

from . import views

app_name = 'comments'
urlpatterns = [
    path('comment/<int:post_pk>', views.comment, name='comment'),
]
