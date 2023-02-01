# Generated by Django 3.0.7 on 2023-01-30 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0005_studentresult'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leavereportstudent',
            old_name='leave_date',
            new_name='date',
        ),
        migrations.AddField(
            model_name='leavereportstudent',
            name='address',
            field=models.CharField(default='Southgate', max_length=100),
        ),
        migrations.AddField(
            model_name='leavereportstudent',
            name='department',
            field=models.CharField(default='Cyber Security', max_length=200),
        ),
        migrations.AddField(
            model_name='leavereportstudent',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leavereportstudent',
            name='faculty',
            field=models.CharField(default='School of Computing', max_length=200),
        ),
        migrations.AddField(
            model_name='leavereportstudent',
            name='full_name',
            field=models.CharField(default='Student Name', max_length=255),
        ),
        migrations.AddField(
            model_name='leavereportstudent',
            name='matric_number',
            field=models.CharField(default='CYS/16/9771', max_length=15),
        ),
        migrations.AddField(
            model_name='leavereportstudent',
            name='phone_number',
            field=models.CharField(default='08021000001', max_length=11),
        ),
        migrations.AddField(
            model_name='leavereportstudent',
            name='session',
            field=models.CharField(default='2020/2021', max_length=10),
        ),
    ]
