from django.db import models
from django.contrib.auth.models import User
from enum import Enum


class RecipeCategory(Enum):
    BREAKFAST = 'Breakfast'
    LUNCH = 'Lunch'
    DINNER = 'Dinner'
    DESSERT = 'Dessert'
    DRINKS = 'Drinks'


class Recipe(models.Model):
    """
    Recipe model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    recipe_category_choices = [(c.value, c.name) for c in RecipeCategory]
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    desc = models.CharField(
        max_length=200, default=('Short description'))
    cooking_time = models.TimeField()
    ingredients = models.TextField()
    steps = models.TextField()
    image = models.ImageField(
       upload_to='images/', default='../default_post_rqlte9', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    category = models.CharField(
        default='Breakfast', max_length=32, choices=recipe_category_choices)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
