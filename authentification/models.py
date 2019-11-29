from django.contrib.auth.models import User
from django.db import models


# Create your models here.

#
# class Professorx(models.Model):
#     prof = models.OneToOneField(User, on_delete=models.CASCADE)


# class Studentx(models.Model):
#     stud = models.OneToOneField(User, on_delete=models.CASCADE)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_professor = models.BooleanField(default=False)
