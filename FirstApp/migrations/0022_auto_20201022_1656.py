# Generated by Django 3.0.3 on 2020-10-22 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstApp', '0021_advice_subtopic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advice',
            name='Subtopic',
            field=models.CharField(choices=[('Scope and Salary', 'Scope and salary'), ('What,how when to prepare', 'What,how when to prepare'), ('From where to prepare', 'From where to prepare'), ('How to apply for jobs', 'How to apply for jobs'), ('Others', 'Others'), ('Resume', 'Resume')], max_length=50),
        ),
    ]