from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
    


class Ingredients(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FoodProduct(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/food_products/', default="static/food_products/default")
    description = models.TextField()
    ingredients = models.ManyToManyField(Ingredients, blank=True)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)
    quantity = models.PositiveBigIntegerField(default=1)
    
class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(FoodProduct, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.CharField(max_length=1000)
    order_datetime = models.DateTimeField()
    pickup_time = models.DateTimeField()
    total = models.DecimalField(max_digits=6, decimal_places=2)