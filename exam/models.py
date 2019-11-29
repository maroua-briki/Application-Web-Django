from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Exam(models.Model):
    name = models.CharField(max_length=100)
    # logo = models.ImageField(upload_to="media/logs/")
    # logo = models.ImageField(upload_to='logs', blank=True, null=True)
    description = models.TextField(max_length=500)
    timer = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    category = models.CharField(max_length=30, default='')
    mode = models.CharField(max_length=20, default='')
    success_score = models.IntegerField(default=70)
    prof = models.ForeignKey(User, on_delete=models.CASCADE, related_name='prof', null=True, blank=True)


    def ___str__(self):
        return self.name


class Question(models.Model):
    ex = models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
    description = models.TextField(max_length=500)
    point = models.CharField(max_length=4)
    header_text = models.TextField(max_length=70)
    footer_text = models.TextField(max_length=70)
    success_message = models.CharField(max_length=30)
    fail_message = models.CharField(max_length=30)
    correct_answer = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.description


class One_answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer_variant = models.TextField(max_length=200)
    answer_description = models.TextField(max_length=200)
    point = models.IntegerField(default=0)
    # is_rightONE = models.BooleanField(default=False)



class Free_Text(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    text = models.TextField(max_length=500)


class Multichoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    multi_variant = models.TextField(max_length=200)
    multi_descp = models.TextField(max_length=200)
    point = models.IntegerField(default=0)


class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='Exam', default=1)
    One_answer = models.ForeignKey(One_answer, on_delete=models.CASCADE, blank=True, null=True)
    multi_choice_answer = models.ForeignKey(Multichoice, on_delete=models.CASCADE, blank=True, null=True)
    free_text = models.CharField(max_length=1000, default='', blank=True, null=True)
    score_question = models.IntegerField(default=0)


class Groupst(models.Model):
    professor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='professor', null=True, blank=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student', blank=True, null=True)
    assigned_exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='assigned_exam', blank=True, null=True)
