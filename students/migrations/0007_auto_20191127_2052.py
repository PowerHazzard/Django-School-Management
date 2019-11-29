# Generated by Django 2.2.7 on 2019-11-27 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0005_auto_20191127_2052'),
        ('students', '0006_student_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='head',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='guide',
        ),
        migrations.AlterField(
            model_name='student',
            name='ac_session',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='admin_tools.AcademicSession'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_tools.Department'),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.ForeignKey(default='1st', on_delete=django.db.models.deletion.CASCADE, to='admin_tools.Semester'),
        ),
        migrations.DeleteModel(
            name='AcademicSession',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Semester',
        ),
    ]
