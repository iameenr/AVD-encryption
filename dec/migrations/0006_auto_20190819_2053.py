# Generated by Django 2.2.4 on 2019-08-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dec', '0005_auto_20190819_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deckey',
            name='id',
            field=models.IntegerField(default=100, primary_key=True, serialize=False),
        ),
    ]