# Generated by Django 4.1.7 on 2023-03-23 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittlelemonAPI', '0005_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]
