# Generated by Django 2.0.7 on 2018-08-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_auto_20180727_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='point',
            field=models.CharField(max_length=4),
        ),
    ]