# Generated by Django 4.1.7 on 2023-03-28 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flexzone', '0017_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]