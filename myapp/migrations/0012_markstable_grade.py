# Generated by Django 4.2.6 on 2024-02-04 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_studenttable_gender_studenttable_student_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='markstable',
            name='Grade',
            field=models.FloatField(null=True),
        ),
    ]
