from django.urls import path
from .views import get_recommendations, mobile, plat_details, view_recommendations

urlpatterns = [
    path("get_recommendations/", get_recommendations, name="get_recommendations"),
    path("view_recommendations/<str:season>/<str:soil_type>/<str:plant_type>/<str:sunlight_type>/<str:watering>/", view_recommendations, name="view_recommendations"),
    path("mobile/", mobile, name="mobile"),
    path("plant-details/<int:plant_id>/", plat_details, name="plant-details"),


]
