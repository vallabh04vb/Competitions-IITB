# Generated by Django 4.2.1 on 2023-11-22 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiapp', '0014_rename_address_socio_quiz_reg_college_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mootcourt_reg',
            old_name='address',
            new_name='College_Name',
        ),
        migrations.RenameField(
            model_name='mootcourt_reg',
            old_name='schoolname',
            new_name='team_leader_Name',
        ),
        migrations.RenameField(
            model_name='socio_quiz_reg',
            old_name='College_Name',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='socio_quiz_reg',
            old_name='team_leader_Name',
            new_name='schoolname',
        ),
        migrations.RemoveField(
            model_name='mootcourt_reg',
            name='POC',
        ),
        migrations.RemoveField(
            model_name='mootcourt_reg',
            name='principal',
        ),
        migrations.RemoveField(
            model_name='mootcourt_reg',
            name='profession',
        ),
        migrations.AddField(
            model_name='socio_quiz_reg',
            name='POC',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='socio_quiz_reg',
            name='principal',
            field=models.CharField(default='', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='socio_quiz_reg',
            name='profession',
            field=models.CharField(default='', max_length=50),
        ),
    ]
