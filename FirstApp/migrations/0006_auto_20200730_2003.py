# Generated by Django 3.0.3 on 2020-07-30 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FirstApp', '0005_mylibrary'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Financial_Succcess_Resources',
            new_name='Financial_Success_Resources',
        ),
        migrations.CreateModel(
            name='Challenge2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Time', models.DateField()),
                ('Book_Title', models.CharField(max_length=75)),
                ('Book_Author', models.CharField(max_length=50)),
                ('Start_Date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Challenge1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Start_Date', models.DateField()),
                ('Hours_spent_learning', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
