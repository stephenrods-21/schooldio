# Generated by Django 3.0.8 on 2020-07-26 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_student_year_in_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
