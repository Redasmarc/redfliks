# Generated by Django 4.1.7 on 2023-03-25 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexzone', '0009_alter_movie_options_rename_movie_name_movie_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='trailer',
            field=models.URLField(blank=True, null=True),
        ),
    ]