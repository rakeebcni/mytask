# Generated by Django 4.2.6 on 2024-02-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_coursetable_studenttable_markstable_gradetable'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetable',
            name='Course_Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='coursetable',
            name='Credit_Hour',
            field=models.IntegerField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='markstable',
            name='CGPA',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='markstable',
            name='Marks',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='Courses',
            field=models.ManyToManyField(null=True, to='myapp.coursetable'),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='Student_Department',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='studenttable',
            name='Student_Name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
