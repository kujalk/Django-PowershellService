# Generated by Django 3.0.6 on 2020-05-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firewall', '0002_auto_20200525_2034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firewallstatus',
            name='Display_Name',
            field=models.CharField(max_length=50),
        ),
    ]
