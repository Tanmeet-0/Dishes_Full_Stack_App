from django.shortcuts import render
from .models import Dish
from django.db.models import F
from django.http import HttpResponse, HttpResponseNotFound
from .serializers import DishSerializer
from rest_framework.renderers import JSONRenderer

# Create your views here.
def dashboard(request):
    all_dishes = DishSerializer(Dish.objects.all().order_by("dishId"),many=True)
    json_data = JSONRenderer().render(all_dishes.data) 
    return HttpResponse(json_data)

def dish_toggle_is_published(request, dish_id):
    dish_filter = Dish.objects.filter(dishId=dish_id)
    if dish_filter.count() == 0:
        return HttpResponseNotFound("Error dishId does not exist")  
    dish = dish_filter[0]
    dish.isPublished = ~ F("isPublished") # apply not operation to isPublished 
    dish.save() 
    return HttpResponse("<h1>Success</h1><br><img src=\"{}\">".format(dish.imageUrl))
