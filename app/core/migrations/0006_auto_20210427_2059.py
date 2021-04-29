# Generated by Django 3.2 on 2021-04-27 20:59

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('core', '0005_auto_20210420_2109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissionrun',
            name='data_privacy_level',
        ),
        migrations.AddField(
            model_name='prediction',
            name='challenge',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.challenge'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='submissionrun',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='AnswerKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('key', models.CharField(max_length=255)),
                ('object_id', models.PositiveIntegerField()),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.challenge')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('input_element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.inputelement')),
            ],
            options={
                'unique_together': {('input_element', 'key')},
            },
        ),
    ]
