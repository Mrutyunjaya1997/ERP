# Generated by Django 3.0 on 2021-06-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210603_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appliedcourses',
            name='apply_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='appliedcourses',
            name='offline',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='appliedcourses',
            name='online',
            field=models.BooleanField(),
        ),
    ]