# Generated by Django 4.2 on 2023-05-19 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_student_my_field_student_prof'),
    ]

    operations = [
        migrations.DeleteModel(
            name='user',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='my_field',
            new_name='verfed',
        ),
    ]
