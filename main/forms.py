from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from click import style
from django import forms
from django.forms import ModelForm, TextInput
from .models import Answer,Question,CustomUser


class AnswerForm(ModelForm):
    class Meta:
        model=Answer
        fields=('detail',)

class QuestionForm(ModelForm):
    class Meta:
        model=Question
        fields=('title','detail','tags')
        

class ProfileForm(ModelForm):
    class Meta:
        model=CustomUser
        fields=('first_name','last_name','username','bio','location')