from django.db import models

# Create your models here.
class Dish(models.Model):
    dishId = models.AutoField(primary_key=True)
    dishName = models.CharField(max_length=100)
    imageUrl = models.CharField(max_length=300)
    isPublished = models.BooleanField()

    def __str__(self):
        return self.dishName
