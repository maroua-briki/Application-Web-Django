# Generated by Django 2.0.7 on 2018-08-29 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0018_auto_20180829_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='success_score',
            field=models.IntegerField(default=70),
        ),
    ]