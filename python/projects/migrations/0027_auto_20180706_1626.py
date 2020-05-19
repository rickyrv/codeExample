# Generated by Django 2.0.5 on 2018-07-06 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0026_auto_20180706_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='admin_approval',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='brief',
            field=models.TextField(max_length=600),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, max_length=600),
        ),
    ]
