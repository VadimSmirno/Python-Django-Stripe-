# Generated by Django 4.1.6 on 2023-02-11 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descriptions', models.TextField()),
                ('price', models.IntegerField(default=0)),
                ('currency', models.CharField(max_length=10)),
            ],
        ),
    ]