# Generated by Django 3.2.18 on 2023-03-08 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='category',
            field=models.CharField(choices=[('Breakfast', 'BREAKFAST'), ('Lunch', 'LUNCH'), ('Dinner', 'DINNER'), ('Dessert', 'DESSERT'), ('Drinks', 'DRINKS')], default='Breakfast', max_length=32),
        ),
    ]
