# Generated by Django 4.2.1 on 2023-11-16 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compiapp', '0004_rename_schoolname_socioexhibition_myschool'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='myschool',
            new_name='schoolname',
        ),
    ]
