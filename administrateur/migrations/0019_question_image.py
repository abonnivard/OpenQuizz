# Generated by Django 4.1.7 on 2023-04-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0018_alter_quizz_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='upload/'),
        ),
    ]