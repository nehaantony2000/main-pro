# Generated by Django 4.1.7 on 2023-04-12 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_remove_applylist_recruiter_notes_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='resume',
        ),
    ]
