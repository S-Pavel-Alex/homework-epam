# Generated by Django 4.0.1 on 2022-01-12 13:16
from datetime import date

from django.db import migrations


def recording(apps, schema_editor):
    Student = apps.get_model('school', 'Student')
    Teacher = apps.get_model('school', 'Teacher')
    Homework = apps.get_model('school', 'Homework')
    HomeworkResult = apps.get_model('school', 'HomeworkResult')
    student = Student(first_name='Pavel', last_name='Smirnov')
    teacher = Teacher(first_name='Ivan', last_name='Petrov')
    homework = Homework(
        text='Learn OOP', created=date.today(), deadline=date.today()
    )
    homework_result = HomeworkResult(
        homework=homework, author=student,
        solution='I finish this homework',
        created=date.today()
    )
    student.save()
    teacher.save()
    homework.save()
    homework_result.save()


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(recording)
    ]
