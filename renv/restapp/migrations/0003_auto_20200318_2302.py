# Generated by Django 3.0.4 on 2020-03-18 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0002_auto_20200318_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
