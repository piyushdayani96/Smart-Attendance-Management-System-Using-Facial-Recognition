# Generated by Django 2.2.2 on 2020-03-01 11:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0011_remove_studentinfo_datee'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='connectdate',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
