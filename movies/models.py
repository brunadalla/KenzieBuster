from django.db import models


class RatingOptions(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, null=True, blank=True, default=None)
    rating = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        choices=RatingOptions.choices,
        default=RatingOptions.G,
    )
    synopsis = models.TextField(null=True, blank=True, default=None)

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies"
    )

    orders = models.ManyToManyField(
        "users.User", through="MovieOrder", related_name="ordered_movies"
    )


class MovieOrder(models.Model):
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="user_orders"
    )
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, related_name="movie_orders"
    )
    buyed_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
