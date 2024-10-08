# Generated by Django 5.1 on 2024-08-26 14:31

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='ProjectSupervisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=256, unique=True)),
                ('firstname', models.CharField(blank=True, max_length=256)),
                ('lastname', models.CharField(blank=True, max_length=256)),
                ('is_coordinator', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('avatar', models.ImageField(default='default_avatar.png', upload_to='images/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('proposal_deadline', models.DateTimeField(blank=True, null=True)),
                ('documentation_deadline', models.DateTimeField(blank=True, null=True)),
                ('implementation_deadline', models.DateTimeField(blank=True, null=True)),
                ('report_deadline', models.DateTimeField(blank=True, null=True)),
                ('progress', models.SmallIntegerField(default=0)),
                ('report_file', models.FileField(blank=True, null=True, upload_to='files/reports/')),
                ('documentation_file', models.FileField(blank=True, null=True, upload_to='files/documentation/')),
                ('platform', models.TextField(blank=True, choices=[('Mobile', 'Mobile'), ('Web', 'Web'), ('Desktop', 'Desktop'), ('CrossPlatform', 'CrossPlatform')], default=None, null=True)),
                ('upgradable', models.BooleanField(default=False)),
                ('comment', models.TextField(blank=True, default='', max_length=500, null=True)),
                ('categories', models.ManyToManyField(blank=True, related_name='projects', to='core.category')),
                ('coordinator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project_supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.projectsupervisor')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=264)),
                ('faculty', models.CharField(blank=True, max_length=256)),
                ('academic_year', models.IntegerField(default=2024)),
                ('project', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='core.project')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264)),
                ('regnumber', models.CharField(max_length=264, unique=True)),
                ('project_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_members', to='core.projectgroup')),
            ],
        ),
    ]
