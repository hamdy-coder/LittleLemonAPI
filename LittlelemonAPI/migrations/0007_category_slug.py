# Generated by Django 4.1.7 on 2023-03-26 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0006_alter_category_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=1),
            preserve_default=False,
        ),
    ]
