# Generated by Django 4.2.1 on 2023-12-07 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compiapp', '0021_rename_phone_hackathonregistration_comments_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mock_parliament_reg',
            old_name='address',
            new_name='College',
        ),
        migrations.RenameField(
            model_name='mock_parliament_reg',
            old_name='schoolname',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='mock_parliament_reg',
            name='POC',
        ),
        migrations.RemoveField(
            model_name='mock_parliament_reg',
            name='principal',
        ),
    ]
