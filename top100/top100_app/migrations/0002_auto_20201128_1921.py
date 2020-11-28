# Generated by Django 3.1.3 on 2020-11-28 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('top100_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='info',
            field=models.CharField(default='Information', max_length=200),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='Name', max_length=30),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='Name', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='Name', max_length=13),
        ),
        migrations.AlterField(
            model_name='gender',
            name='name',
            field=models.CharField(default='Name', max_length=30),
        ),
    ]
