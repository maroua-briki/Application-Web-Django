# Generated by Django 2.0.7 on 2018-08-29 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0016_one_answer_is_rightanswer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='one_answer',
            old_name='is_rightANSWER',
            new_name='is_rightONE',
        ),
        migrations.AddField(
            model_name='multichoice',
            name='is_rightMULTI',
            field=models.BooleanField(default=False),
        ),
    ]
