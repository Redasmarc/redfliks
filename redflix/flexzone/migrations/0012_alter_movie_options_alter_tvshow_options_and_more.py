# Generated by Django 4.1.7 on 2023-03-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexzone', '0011_movie_status_alter_movie_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='movie',
            options={'ordering': ['title', 'description', 'genres__genre_name', 'producers__producer_f_name', 'producers__producer_l_name', 'release_date', 'actors__actor_f_name', 'actors__actor_l_name']},
        ),
        migrations.AlterModelOptions(
            name='tvshow',
            options={'ordering': ['show_name', 'description', 'season', 'episode', 'genres__genre_name', 'producers__producer_f_name', 'producers__producer_l_name', 'release_date', 'actors__actor_f_name', 'actors__actor_l_name']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['email', 'password', 'first_name', 'last_name', 'phone_number']},
        ),
        migrations.RemoveField(
            model_name='movie',
            name='subscription_pack',
        ),
        migrations.RemoveField(
            model_name='tvshow',
            name='subscription_pack',
        ),
        migrations.RemoveField(
            model_name='user',
            name='subscription',
        ),
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('-', '---------'), ('n', 'Nitflex'), ('h', 'HPO'), ('d', 'Disnep+')], default='-', max_length=1, verbose_name='group'),
        ),
        migrations.DeleteModel(
            name='SubscriptionPack',
        ),
    ]
