# Generated by Django 2.0.7 on 2018-07-23 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentification', '0002_auto_20180723_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.TextField(max_length=50)),
                ('name', models.CharField(max_length=45)),
                ('surname', models.CharField(max_length=45)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('state', models.CharField(max_length=250)),
                ('phone_number', models.CharField(blank=True, max_length=13)),
                ('is_professor', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
