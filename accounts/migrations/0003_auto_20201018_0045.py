# Generated by Django 3.0.7 on 2020-10-17 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201012_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='Category',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='Courier',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='WorkHour',
        ),
    ]