# Generated by Django 3.0.1 on 2020-06-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='moves',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('move_name', models.CharField(max_length=20, unique=True)),
                ('contact_format', models.CharField(max_length=20)),
                ('move_type', models.CharField(max_length=20)),
                ('power', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='is_legendary',
            field=models.BooleanField(),
        ),
    ]