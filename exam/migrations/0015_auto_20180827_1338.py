# Generated by Django 2.0.7 on 2018-08-27 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0014_groupst_assigned_exam'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='mode',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='groupst',
            name='assigned_exam',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_exam', to='exam.Exam'),
        ),
    ]
