# Generated by Django 3.2.6 on 2021-09-07 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('environment_education', '0001_initial'),
        ('persons', '0002_alter_student_rented_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='college',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_college', to='environment_education.college'),
        ),
    ]