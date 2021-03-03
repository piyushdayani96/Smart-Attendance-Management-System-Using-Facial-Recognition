# Generated by Django 2.2.6 on 2019-11-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generalzone', '0002_auto_20191114_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='imagename',
            field=models.CharField(default=0, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentinfo',
            name='videofile',
            field=models.FileField(null=True, upload_to='images/', verbose_name=''),
        ),
    ]
