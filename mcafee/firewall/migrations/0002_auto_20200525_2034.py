# Generated by Django 3.0.6 on 2020-05-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firewall', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firewallstatus',
            name='Date',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='firewallstatus',
            name='Service_Name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='firewallstatus',
            name='Status',
            field=models.CharField(max_length=20),
        ),
    ]
