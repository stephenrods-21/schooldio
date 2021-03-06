# Generated by Django 3.0.8 on 2020-07-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=20)),
                ('max_students', models.PositiveIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
