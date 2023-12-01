# Generated by Django 4.2.7 on 2023-12-01 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_collection_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='image',
            field=models.ImageField(max_length=255, null=True, upload_to='images'),
        ),
    ]
