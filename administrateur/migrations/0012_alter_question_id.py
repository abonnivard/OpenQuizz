# Generated by Django 4.1.7 on 2023-03-31 08:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0011_quizz_numero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
