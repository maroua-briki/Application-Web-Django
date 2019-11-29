from django.contrib import admin

from .models import Exam, Question, One_answer, Free_Text, Multichoice, Answer, Groupst

# Register your models here.
admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(One_answer)
admin.site.register(Free_Text)
admin.site.register(Multichoice)
admin.site.register(Answer)
admin.site.register(Groupst)
