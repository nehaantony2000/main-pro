# Generated by Django 4.1.7 on 2023-04-01 10:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Company', '0003_alter_jobdetails_jobtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=30, unique=True)),
                ('duration', models.CharField(max_length=50, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('slug', models.SlugField()),
                ('desc', models.TextField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('last_date', models.DateField()),
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Courses',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('desp', models.TextField(blank=True, max_length=3000)),
                ('slug', models.SlugField()),
                ('video', models.FileField(upload_to='videos')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.courses')),
            ],
            options={
                'verbose_name': 'Videos',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='SavedJobs',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_saved', models.BooleanField(default=False)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_job', to='Company.jobdetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to=settings.AUTH_USER_MODEL)),
            ],
        ),
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
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satisfaction', models.CharField(choices=[('very-satisfied', 'Very satisfied'), ('satisfied', 'Satisfied'), ('neutral', 'Neutral'), ('dissatisfied', 'Dissatisfied'), ('very-dissatisfied', 'Very dissatisfied')], max_length=50)),
                ('recommendation', models.CharField(choices=[('very-likely', 'Very likely'), ('likely', 'Likely'), ('neutral', 'Neutral'), ('unlikely', 'Unlikely'), ('very-unlikely', 'Very unlikely')], max_length=50)),
                ('likes', models.TextField()),
                ('improvements', models.TextField()),
                ('sentiment', models.FloatField()),
                ('feedbackdate', models.DateField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.courses')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Course_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purhase_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Employee.courses')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Applylist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education', models.CharField(default='', max_length=200)),
                ('minsalary', models.CharField(default='', max_length=20)),
                ('maxsalary', models.CharField(default='', max_length=20)),
                ('resumes', models.FileField(blank=True, null=True, upload_to='AppliedResume')),
                ('applieddate', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=True, verbose_name='status')),
                ('accept', models.BooleanField(default=True, verbose_name='accept')),
                ('reject', models.BooleanField(default=True, verbose_name='reject')),
                ('applied', models.BooleanField(default=True, verbose_name='applied')),
                ('cand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company.jobdetails')),
            ],
        ),
    ]
