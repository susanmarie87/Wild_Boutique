# Generated by Django 3.2 on 2021-12-29 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20211214_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default='2021-01-01 06:00:00.000000-08:00'),
            preserve_default=False,
        ),
    ]
