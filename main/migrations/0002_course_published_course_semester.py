# Generated by Django 4.0.4 on 2024-05-14 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='semester',
            field=models.CharField(default='Fall 2023', max_length=255),
        ),
    ]
