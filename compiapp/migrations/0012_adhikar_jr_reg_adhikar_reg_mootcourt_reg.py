# Generated by Django 4.2.1 on 2023-11-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiapp', '0011_spf_reg'),
    ]

    operations = [
        migrations.CreateModel(
            name='adhikar_jr_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=12)),
                ('City', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('profession', models.CharField(default='', max_length=50)),
                ('principal', models.CharField(default='', max_length=50, null=True)),
                ('POC', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='adhikar_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=12)),
                ('City', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('profession', models.CharField(default='', max_length=50)),
                ('principal', models.CharField(default='', max_length=50, null=True)),
                ('POC', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='mootcourt_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schoolname', models.CharField(default='', max_length=200)),
                ('address', models.CharField(default='', max_length=200)),
                ('email', models.CharField(default='', max_length=254)),
                ('phone', models.CharField(default='', max_length=12)),
                ('City', models.CharField(default='', max_length=50)),
                ('state', models.CharField(default='', max_length=50)),
                ('profession', models.CharField(default='', max_length=50)),
                ('principal', models.CharField(default='', max_length=50, null=True)),
                ('POC', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
