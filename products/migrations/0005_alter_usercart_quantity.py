# Generated by Django 4.1.3 on 2022-12-29 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_remove_usercart_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercart',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
