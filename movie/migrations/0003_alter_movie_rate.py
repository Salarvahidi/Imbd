# Generated by Django 4.1.7 on 2024-05-18 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='rate',
            field=models.IntegerField(default=10, verbose_name='Rate'),
        ),
    ]
