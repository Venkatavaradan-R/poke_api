# Generated by Django 3.0.1 on 2020-06-21 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0003_moves_accuracy'),
    ]

    operations = [
        migrations.AddField(
            model_name='moves',
            name='move_id',
            field=models.IntegerField(default=0, unique=True),
        ),
    ]
