# Generated by Django 4.1.7 on 2023-03-04 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexzone', '0002_actor_genre_producer_movie'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['movie_name', 'description', 'genres__genre_name', 'producers__producer_f_name', 'producers__producer_l_name', 'release_date', 'actors__actor_f_name', 'actors__actor_l_name']},
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(verbose_name='publish date'),
        ),
    ]
