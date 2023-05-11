# Generated by Django 4.1.7 on 2023-05-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0011_alter_applylist_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applylist',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pending'), ('REJECTED', 'Rejected'), ('SELECTED', 'Selected'), ('INTERVIEW SHEDULED', 'Interview Sheduled')], default='PENDING', max_length=20),
        ),
    ]
