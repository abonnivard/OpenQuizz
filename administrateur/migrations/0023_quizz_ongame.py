# Generated by Django 4.1.7 on 2023-04-06 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0022_delete_theme_question_theme'),
    ]

    operations = [
        migrations.AddField(
            model_name='quizz',
            name='onGame',
            field=models.BooleanField(default=False),
        ),
    ]
