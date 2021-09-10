# Generated by Django 3.2.5 on 2021-08-31 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20210806_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evaluation',
            name='status',
            field=models.CharField(choices=[('FAILURE', 'Failure'), ('SUCCESS', 'Success'), ('PENDING', 'Pending'), ('RUNNING', 'Running')], default='PENDING', max_length=25),
        ),
        migrations.AlterField(
            model_name='submissionrun',
            name='status',
            field=models.CharField(choices=[('FAILURE', 'Failure'), ('SUCCESS', 'Success'), ('PENDING', 'Pending'), ('RUNNING', 'Running')], max_length=25),
        ),
    ]