# Generated by Django 2.0.5 on 2018-07-19 12:41

from django.db import migrations, models
import forgeplatform.projects.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0028_auto_20180714_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemwork',
            name='picture',
            field=models.FileField(upload_to=forgeplatform.projects.models.project_media_path),
        ),
    ]