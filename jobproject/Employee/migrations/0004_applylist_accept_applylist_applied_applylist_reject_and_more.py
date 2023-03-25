# Generated by Django 4.1.7 on 2023-03-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0003_appliedjobs_accept_appliedjobs_applied_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='applylist',
            name='accept',
            field=models.BooleanField(default=True, verbose_name='accept'),
        ),
        migrations.AddField(
            model_name='applylist',
            name='applied',
            field=models.BooleanField(default=True, verbose_name='applied'),
        ),
        migrations.AddField(
            model_name='applylist',
            name='reject',
            field=models.BooleanField(default=True, verbose_name='reject'),
        ),
        migrations.AddField(
            model_name='applylist',
            name='status',
            field=models.BooleanField(default=True, verbose_name='status'),
        ),
    ]
