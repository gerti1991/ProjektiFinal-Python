# Generated by Django 4.0.3 on 2022-03-27 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0002_alter_attendance_id_alter_department_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp706', max_length=70),
        ),
    ]
