# Generated by Django 2.0.5 on 2018-06-20 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0018_auto_20180620_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileitemethadd',
            name='address',
            field=models.CharField(max_length=42),
        ),
    ]