# Generated by Django 2.0.5 on 2018-05-23 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20180523_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='folder',
            options={'ordering': ['-title']},
        ),
    ]
