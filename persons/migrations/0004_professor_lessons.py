# Generated by Django 3.2.6 on 2021-09-07 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('environment_education', '0001_initial'),
        ('persons', '0003_alter_student_college'),
    ]

    operations = [
        migrations.AddField(
            model_name='professor',
            name='lessons',
            field=models.ManyToManyField(blank=True, null=True, related_name='professor_lessons', to='environment_education.Lesson'),
        ),
    ]
