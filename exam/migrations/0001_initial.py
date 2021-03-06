# Generated by Django 2.0.7 on 2018-07-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admId', models.CharField(max_length=20)),
                ('admName', models.CharField(max_length=20)),
                ('admPassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='FillBlank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fbCourse', models.CharField(max_length=20)),
                ('fbGrade', models.CharField(max_length=5)),
                ('fbContent', models.CharField(max_length=500)),
                ('fbAnswer1', models.CharField(max_length=100)),
                ('fbAnswer2', models.CharField(blank=True, max_length=100, null=True)),
                ('fbAnswer3', models.CharField(blank=True, max_length=100, null=True)),
                ('fbAnswer4', models.CharField(blank=True, max_length=100, null=True)),
                ('fbAnswer5', models.CharField(blank=True, max_length=100, null=True)),
                ('fbAnswer6', models.CharField(blank=True, max_length=100, null=True)),
                ('fbAnswer7', models.CharField(blank=True, max_length=100, null=True)),
                ('fbAnswer8', models.CharField(blank=True, max_length=100, null=True)),
                ('fbAnswer9', models.CharField(blank=True, max_length=100, null=True)),
                ('fbAnswer10', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShortAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saCourse', models.CharField(max_length=20)),
                ('saGrade', models.CharField(max_length=5)),
                ('saContent', models.CharField(max_length=500)),
                ('saAnswer', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuId', models.CharField(max_length=20)),
                ('stuName', models.CharField(max_length=20)),
                ('stuPassword', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teaId', models.CharField(max_length=20)),
                ('teaName', models.CharField(max_length=20)),
                ('teaPassword', models.CharField(max_length=30)),
            ],
        ),
    ]
