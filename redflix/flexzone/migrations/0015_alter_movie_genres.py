# Generated by Django 4.1.7 on 2023-03-27 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexzone', '0014_alter_movie_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='genre', to='flexzone.genre', verbose_name='Genres'),
        ),
    ]