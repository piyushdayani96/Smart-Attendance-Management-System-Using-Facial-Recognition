# Generated by Django 2.2.2 on 2020-03-01 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0009_auto_20200301_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentinfo',
            old_name='connectdate',
            new_name='datee',
        ),
    ]
