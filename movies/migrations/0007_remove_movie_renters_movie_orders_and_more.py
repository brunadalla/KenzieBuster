# Generated by Django 4.1.3 on 2022-12-08 15:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("movies", "0006_movieorder_movie_renters"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="movie",
            name="renters",
        ),
        migrations.AddField(
            model_name="movie",
            name="orders",
            field=models.ManyToManyField(
                related_name="ordered_movies",
                through="movies.MovieOrder",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="movieorder",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="movie_orders",
                to="movies.movie",
            ),
        ),
        migrations.AlterField(
            model_name="movieorder",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_orders",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
