# Generated by Django 3.2.7 on 2021-10-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesdata',
            name='typ',
            field=models.CharField(default='action', max_length=200),
        ),
    ]