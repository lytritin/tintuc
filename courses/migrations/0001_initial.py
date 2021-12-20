# Generated by Django 3.2.7 on 2021-09-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('educator', models.CharField(max_length=100)),
                ('num_lessons', models.PositiveSmallIntegerField(default=0)),
                ('excerpt', models.TextField(max_length=300)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='course_pictures')),
            ],
        ),
    ]
