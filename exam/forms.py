from django import forms
from django.forms import ModelForm
from .models import Exam, Question


class Create_examForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = {'name', 'description', 'timer', 'is_active', 'category', }

#
# class Create_questionForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = {'description', 'point', 'header_text', 'footer_text', 'success_message', 'fail_message'}
