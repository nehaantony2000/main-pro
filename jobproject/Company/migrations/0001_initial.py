# Generated by Django 4.1.7 on 2023-03-20 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='JobDetails',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('jobname', models.CharField(default='', max_length=250)),
                ('companyname', models.CharField(default='', max_length=250)),
                ('jobtype', models.CharField(choices=[('Part-Time', 'Part-Time'), ('Full-Time', 'Full-Time'), ('Internship', 'Internship')], default='', max_length=250)),
                ('category', models.CharField(choices=[('Web Developers', 'Web Developers'), ('Mobile Developers', 'Mobile Developers'), ('Designers & Creatives', 'Designers & Creatives'), ('Writers', 'Writers'), ('Virtual Assistants', 'Virtual Assistants'), ('Accountants & Consultants', 'Accountants & Consultants'), ('Sales & Marketing Experts', 'Sales & Marketing Experts'), ('Customer Service Agents', 'Customer Service Agents')], default='', max_length=250)),
                ('companyaddress', models.CharField(default='', max_length=250)),
                ('jobdescription', models.TextField(default='', max_length=1500)),
                ('qualification', models.TextField(default='', max_length=1500)),
                ('responsibility', models.TextField(default='', max_length=1500)),
                ('location', models.CharField(default='', max_length=250)),
                ('companywebsite', models.CharField(default='', max_length=20)),
                ('companycontact', models.BigIntegerField(default=0)),
                ('salarypackage', models.CharField(default='', max_length=40)),
                ('experience', models.CharField(default='', max_length=40)),
                ('tagline', models.CharField(default='', max_length=100)),
                ('enddate', models.DateField(blank=True, null=True)),
                ('logo', models.ImageField(null=True, upload_to='logos')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('email', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
