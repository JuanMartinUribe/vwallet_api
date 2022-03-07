# Generated by Django 4.0.3 on 2022-03-07 16:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pocket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('quantity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('available', 'Available'), ('blocked', 'Blocked')], default='available', max_length=10)),
                ('main_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pockets', to='vwallet_main.mainuser')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]