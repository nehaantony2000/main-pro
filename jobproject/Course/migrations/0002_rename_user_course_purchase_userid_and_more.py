# Generated by Django 4.1.7 on 2023-03-20 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Course', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_purchase',
            old_name='user',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='courses',
            old_name='user',
            new_name='userid',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='user',
            new_name='userid',
        ),
    ]
