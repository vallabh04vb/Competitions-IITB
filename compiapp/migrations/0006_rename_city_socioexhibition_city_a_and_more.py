# Generated by Django 4.2.1 on 2023-11-16 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('compiapp', '0005_rename_myschool_socioexhibition_schoolname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='City',
            new_name='City_a',
        ),
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='POC',
            new_name='POC_a',
        ),
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='address',
            new_name='address_a',
        ),
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='email',
            new_name='email_a',
        ),
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='phone',
            new_name='phone_a',
        ),
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='principal',
            new_name='principal_a',
        ),
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='profession',
            new_name='profession_a',
        ),
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='schoolname',
            new_name='schoolname_a',
        ),
        migrations.RenameField(
            model_name='socioexhibition',
            old_name='state',
            new_name='state_a',
        ),
    ]
