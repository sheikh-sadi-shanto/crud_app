# Generated by Django 4.1.7 on 2023-07-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr1', '0004_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]