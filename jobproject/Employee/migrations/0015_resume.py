# Generated by Django 4.1.7 on 2023-03-30 11:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0014_delete_resume'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('res_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=100)),
                ('position', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('carobj', models.TextField(blank=True, max_length=300)),
                ('college', models.CharField(blank=True, max_length=200)),
                ('plus', models.CharField(blank=True, max_length=200)),
                ('ten', models.CharField(blank=True, max_length=200)),
                ('projects', models.TextField(blank=True, max_length=100)),
                ('certi', models.TextField(blank=True, max_length=100)),
                ('achi', models.TextField(blank=True, max_length=100)),
                ('interns', models.TextField(blank=True, max_length=100)),
                ('refe', models.TextField(blank=True, max_length=100)),
                ('phone', models.TextField(blank=True, max_length=100, null=True)),
                ('address', models.TextField(blank=True, max_length=100)),
                ('strength', models.TextField(blank=True, max_length=100, null=True)),
                ('skills', models.TextField(blank=True, max_length=100, null=True)),
                ('lang', models.TextField(blank=True, max_length=100, null=True)),
                ('hob', models.TextField(blank=True, max_length=100, null=True)),
                ('soci', models.CharField(blank=True, max_length=100)),
                ('coun', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=0, verbose_name='status')),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=100, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
