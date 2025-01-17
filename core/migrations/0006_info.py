# Generated by Django 5.0.4 on 2024-04-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_faq_alter_fake_news_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('info', models.TextField()),
                ('facebook', models.URLField()),
                ('instagram', models.URLField()),
                ('twitter', models.URLField()),
                ('tiktok', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('website', models.URLField()),
            ],
        ),
    ]
