# Generated by Django 5.0.4 on 2024-04-18 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='featured',
            field=models.BooleanField(default=False),
        ),
    ]
