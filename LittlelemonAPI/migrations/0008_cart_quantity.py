# Generated by Django 4.1.7 on 2023-05-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0007_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.SmallIntegerField(default=1),
        ),
    ]
