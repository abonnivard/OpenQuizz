# Generated by Django 4.1.7 on 2023-03-24 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrateur', '0007_question_numero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
    ]
