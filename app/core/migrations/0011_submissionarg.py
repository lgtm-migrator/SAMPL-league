# Generated by Django 3.2.6 on 2021-09-10 21:28

import core.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20210907_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmissionArg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.SlugField(db_index=False)),
                ('string_value', models.TextField(blank=True, null=True)),
                ('file_value', models.FileField(blank=True, null=True)),
                ('submission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='args', to='core.submission')),
            ],
            options={
                'unique_together': {('submission', 'key')},
            },
        ),
    ]