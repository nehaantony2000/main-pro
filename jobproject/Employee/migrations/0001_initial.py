# Generated by Django 4.1.7 on 2023-03-20 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('carobj', models.TextField(blank=True)),
                ('college', models.CharField(blank=True, max_length=100)),
                ('plus', models.CharField(blank=True, max_length=100)),
                ('ten', models.CharField(blank=True, max_length=100)),
                ('projects', models.TextField(blank=True)),
                ('certi', models.TextField(blank=True)),
                ('achi', models.TextField(blank=True)),
                ('interns', models.TextField(blank=True)),
                ('refe', models.TextField(blank=True)),
                ('phone', models.IntegerField(blank=True, default=0, null=True)),
                ('address', models.TextField(blank=True)),
                ('strength', models.TextField(blank=True, null=True)),
                ('skills', models.TextField(blank=True, null=True)),
                ('lang', models.TextField(blank=True, null=True)),
                ('hob', models.TextField(blank=True, null=True)),
                ('soci', models.CharField(blank=True, max_length=100)),
                ('coun', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=0, verbose_name='status')),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SavedJobs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_job', to='Company.jobdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(default='', max_length=200)),
                ('minsalary', models.CharField(default='', max_length=20)),
                ('maxsalary', models.CharField(default='', max_length=20)),
                ('resume', models.FileField(upload_to='resume')),
                ('applieddate', models.DateTimeField(auto_now_add=True)),
                ('cand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.jobdetails')),
            ],
        ),
        migrations.CreateModel(
            name='AppliedJobs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_job', to='Company.jobdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applied_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
