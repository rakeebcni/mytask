# Generated by Django 5.0.1 on 2024-01-31 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_job_title_addjob_myjob_title'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='addjob',
            new_name='AddJobTable',
        ),
    ]