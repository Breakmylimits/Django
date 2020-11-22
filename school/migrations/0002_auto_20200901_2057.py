# Generated by Django 3.0 on 2020-09-01 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allstudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('ม.1', 'ม.1'), ('ม.2', 'ม.2'), ('ม.3', 'ม.2'), ('ม.4', 'ม.4'), ('ม.5', 'ม.5'), ('ม.6', 'ม.6')], default='ม.1', max_length=100)),
                ('student_name', models.CharField(max_length=200)),
                ('student_id', models.CharField(max_length=200)),
                ('student_tel', models.CharField(blank=True, max_length=200, null=True)),
                ('parent_name', models.CharField(blank=True, max_length=200, null=True)),
                ('parent_tel', models.CharField(blank=True, max_length=200, null=True)),
                ('other', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='examscore',
            name='subject',
            field=models.CharField(choices=[('คณิตศาสตร์', 'คณิตศาสตร์'), ('วิทยาศาสตร์', 'วิทยาศาสตร์'), ('ศิลป', 'ศิลป'), ('ภาษาอังกฤษ', 'ภาษาอังกฤษ'), ('ฟิสิกส์', 'ฟิสิกส์'), ('ชีววิทยา', 'ชีววิทยา')], default='คณิตศาสตร์', max_length=200),
        ),
    ]
