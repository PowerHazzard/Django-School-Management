# Generated by Django 2.2.13 on 2020-12-19 11:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('academics', '0010_auto_20201219_0025'),
        ('students', '0020_auto_20201219_0054'),
        ('result', '0003_auto_20201207_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('exam_name', models.CharField(choices=[('Mid Term', 'm'), ('Final', 'f')], max_length=1)),
                ('exam_date', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('practical_marks', models.SmallIntegerField(blank=True, null=True)),
                ('theory_marks', models.SmallIntegerField(blank=True, null=True)),
                ('total_marks', models.SmallIntegerField(blank=True, null=True)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Semester')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to='students.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Subject')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
