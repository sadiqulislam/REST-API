# Generated by Django 3.0.4 on 2020-03-19 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0003_auto_20200318_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='image',
            field=models.ImageField(default='Images/None/noimg.jpg', upload_to='Images/'),
        ),
    ]
