# Generated by Django 3.1.2 on 2020-12-15 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top100_app', '0008_auto_20201215_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='description',
            field=models.CharField(default='Description', max_length=300),
        ),
    ]
