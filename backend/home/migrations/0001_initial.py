# Generated by Django 4.2 on 2023-05-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adresse_email', models.CharField(max_length=50)),
                ('passe', models.CharField(max_length=20)),
            ],
        ),
    ]
