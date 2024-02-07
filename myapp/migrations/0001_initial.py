# Generated by Django 5.0.1 on 2024-01-31 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addjob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Job_Title', models.CharField(max_length=100)),
                ('Company_Name', models.CharField(max_length=100)),
                ('Company_Description', models.CharField(max_length=100)),
                ('Qualifications', models.CharField(max_length=100)),
                ('Location_Name', models.CharField(max_length=100)),
                ('Job_Description', models.CharField(max_length=100)),
                ('Application_Deadline', models.CharField(max_length=100)),
            ],
        ),
    ]