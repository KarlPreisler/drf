from django.db import models
from django.contrib.auth.models import User
from recipes.models import Recipe


class Comment(models.Model):
    """
    Comment model, related to User and Recipe
    """
    RATING_CHOICES = (
        (0, '0'),
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content
