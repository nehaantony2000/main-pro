# Generated by Django 4.1.7 on 2023-03-23 10:18

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('contact', models.BigIntegerField(default=0)),
                ('address', models.CharField(default='', max_length=150)),
                ('country', django_countries.fields.CountryField(max_length=50)),
                ('gender', models.CharField(default='None', max_length=50)),
                ('dob', models.DateField(blank=True, null=True)),
                ('language', models.CharField(choices=[('English', 'English'), ('Malayalam', 'Malayalam'), ('Hindi', 'Hindi')], default='', max_length=50)),
                ('skills', models.CharField(choices=[('Django', 'Django'), ('Html', 'Html'), ('PHP', 'PHP'), ('Java', 'Java')], default='', max_length=50)),
                ('state', models.CharField(choices=[('kerala', 'kerala'), ('demo', 'demo'), ('None', 'None')], default='', max_length=50)),
                ('district', models.CharField(choices=[('Kozhikode', 'Kozhikode'), ('Malappuram', 'Malappuram'), ('Kannur', 'Kannur'), ('Trivandrum', 'Trivandrum'), ('Palakkad', 'Palakkad'), ('Thrissur', 'Thrissur'), ('Kottayam', 'Kottayam'), ('Alappuzha', 'Alappuzha'), ('Idukki', 'Idukki'), ('Kollam', 'Kollam'), ('Ernakulam', 'Ernakulam'), ('Wayanad', 'Wayanad'), ('Kasaragod', 'Kasaragod'), ('Pathanamthitta', 'Pathanamthitta'), ('Thiruvananthapuram', 'Thiruvananthapuram'), ('None', 'None')], default='', max_length=50)),
                ('profilepic', models.ImageField(blank=True, null=True, upload_to='Profile')),
                ('Resume', models.FileField(blank=True, null=True, upload_to='Resume')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('last_login', models.DateTimeField(auto_now_add=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_company', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('is_employee', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
