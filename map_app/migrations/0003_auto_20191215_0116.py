# Generated by Django 3.0 on 2019-12-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map_app', '0002_auto_20191215_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='income',
            name='income',
            field=models.FloatField(),
        ),
    ]