# Generated by Django 3.2.5 on 2023-02-01 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_advertdata_extras'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertdata',
            name='extras',
        ),
    ]
