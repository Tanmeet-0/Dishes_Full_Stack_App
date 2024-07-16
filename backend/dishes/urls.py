from django.urls import path

from . import views

urlpatterns = [
    path("",views.dashboard, name="dashboard"),
    path("toggle_publish/<int:dish_id>/",views.dish_toggle_is_published,name="toggle_publish")
]