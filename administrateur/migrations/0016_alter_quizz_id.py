# Generated by Django 4.1.7 on 2023-03-31 08:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0015_quizz_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizz',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
