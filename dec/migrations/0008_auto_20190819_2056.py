# Generated by Django 2.2.4 on 2019-08-19 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dec', '0007_auto_20190819_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deckey',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
