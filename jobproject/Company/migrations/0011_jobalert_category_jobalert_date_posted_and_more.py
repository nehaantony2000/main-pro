# Generated by Django 4.1.7 on 2023-05-16 16:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Company', '0010_jobalert'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobalert',
            name='category',
            field=models.CharField(choices=[('accounting-finance', 'Accounting & Finance'), ('administrative', 'Administrative'), ('customer-service', 'Customer Service'), ('engineering', 'Engineering'), ('healthcare', 'Healthcare'), ('human-resources', 'Human Resources'), ('information-technology', 'Information Technology'), ('marketing', 'Marketing'), ('sales', 'Sales')], default='', max_length=250),
        ),
        migrations.AddField(
            model_name='jobalert',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='jobalert',
            name='jobtype',
            field=models.CharField(choices=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time'), ('Internship', 'Internship'), ('Freelance', 'Freelance')], default='', max_length=250),
        ),
        migrations.AddField(
            model_name='jobalert',
            name='location',
            field=models.CharField(default='', max_length=250),
        ),
    ]
