# Generated by Django 4.1.7 on 2023-08-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pr1', '0005_alter_person_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('pic', models.FileField(upload_to='file')),
            ],
        ),
    ]