# Generated by Django 4.0.2 on 2022-03-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20211125_2146'),
    ]

    operations = [
        migrations.AddField(
            model_name='container',
            name='container_type',
            field=models.CharField(choices=[('Docker', 'Docker'), ('Singularity', 'Singularity')], help_text='State the type of container image you are submitting `Docker` or `Singularity`.', max_length=255, null=True),
        ),
    ]
