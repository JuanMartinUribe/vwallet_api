# Generated by Django 4.0.3 on 2022-03-10 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vwallet_main', '0003_remove_pocket_user_mainuser_username_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mainuser',
            name='username',
        ),
    ]
