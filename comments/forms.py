#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Author:Mikigo
@Date  :2022/5/18 22:40
@Desc  :
"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
