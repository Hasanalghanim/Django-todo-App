# Generated by Django 3.1.2 on 2020-10-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0017_auto_20201024_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date_completed',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
