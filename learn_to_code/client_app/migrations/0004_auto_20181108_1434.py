# Generated by Django 2.1.2 on 2018-11-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_app', '0003_auto_20181024_2138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientprofileinfo',
            name='completed_lessons',
        ),
        migrations.AddField(
            model_name='clientprofileinfo',
            name='completed_lessons',
            field=models.ManyToManyField(to='client_app.Lesson'),
        ),
    ]