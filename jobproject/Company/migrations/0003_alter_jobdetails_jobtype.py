# Generated by Django 4.1.7 on 2023-03-29 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0002_selected_applicants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetails',
            name='jobtype',
            field=models.CharField(choices=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time'), ('Internship', 'Internship'), ('Freelance', 'Freelance')], default='', max_length=250),
        ),
    ]
