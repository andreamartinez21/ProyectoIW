# Generated by Django 3.1.3 on 2020-11-25 09:48

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(blank=True, max_length=31)),
                ('mail', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]
