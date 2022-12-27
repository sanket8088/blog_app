# Generated by Django 4.1.3 on 2022-12-27 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_managers_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='is_default',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='nickname',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]
