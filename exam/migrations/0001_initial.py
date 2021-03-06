# Generated by Django 2.0.7 on 2018-07-24 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='media/logs/')),
                ('description', models.TextField(max_length=500)),
                ('timer', models.DurationField(default=0)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Free_Text',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Multichoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multi_variant', models.TextField(max_length=200)),
                ('multi_descp', models.TextField(max_length=200)),
                ('point', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='One_answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_variant', models.TextField(max_length=200)),
                ('answer_description', models.TextField(max_length=200)),
                ('point', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
                ('point', models.IntegerField(default=0)),
                ('header_text', models.TextField(max_length=70)),
                ('footer_text', models.TextField(max_length=70)),
                ('success_message', models.CharField(max_length=30)),
                ('fail_message', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='one_answer',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Question'),
        ),
        migrations.AddField(
            model_name='multichoice',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Question'),
        ),
        migrations.AddField(
            model_name='free_text',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.Question'),
        ),
    ]
