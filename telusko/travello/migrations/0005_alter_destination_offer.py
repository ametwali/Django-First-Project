# Generated by Django 4.2 on 2023-04-11 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0004_destination_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='offer',
            field=models.BooleanField(default=False),
        ),
    ]
