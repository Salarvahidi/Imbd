# Generated by Django 4.1.7 on 2024-05-18 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Director name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Director last name')),
                ('birth_date', models.DateField(verbose_name='Director birth date')),
                ('is_active', models.BooleanField(default=True, verbose_name=' Is active')),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directors',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('year', models.IntegerField(verbose_name='Year')),
                ('rate', models.IntegerField(blank=True, null=True, verbose_name='Rate')),
                ('director', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.director', verbose_name='Director')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]