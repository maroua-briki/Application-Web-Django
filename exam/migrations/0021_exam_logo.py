# Generated by Django 2.0.7 on 2018-08-31 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0020_exam_is_passed'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='logs'),
        ),
    ]
