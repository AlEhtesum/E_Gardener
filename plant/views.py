from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RecommendationForm
from .models import Plant
from django.shortcuts import render

@login_required(login_url="signin")
def get_recommendations(request):
    form = RecommendationForm()

    if request.method == "POST":
        form = RecommendationForm(request.POST)
        if form.is_valid():
            season = form.cleaned_data["season"]
            soil_type = form.cleaned_data["soil_type"]
            plant_type = form.cleaned_data["plant_type"]
            sunlight_type = form.cleaned_data["sunlight_type"]
            watering = form.cleaned_data["watering"]

            return redirect(
                "view_recommendations",
                season=season,
                soil_type=soil_type,
                plant_type=plant_type,
                sunlight_type=sunlight_type,
                watering=watering,
            )

    return render(request, "recommendation/get_recommendations.html", {"form": form})


def view_recommendations(request, season, soil_type, plant_type, sunlight_type, watering):
    matching_plants = Plant.objects.filter(
                season__iexact=season, soil_type__iexact=soil_type, plant_type__iexact=plant_type, sunlight_type__iexact = sunlight_type, watering__iexact=watering
            )

    recommendations = matching_plants

    return render(
        request,
        "recommendation/recommendations.html",
        {"recommendations": recommendations},
    )

def mobile(request):
    form = RecommendationForm()

    if request.method == "POST":
        form = RecommendationForm(request.POST)
        if form.is_valid():
            season = form.cleaned_data["season"]
            soil_type = form.cleaned_data["soil_type"]
            plant_type = form.cleaned_data["plant_type"]
            
            matching_plants = Plant.objects.filter(
                season__iexact=season, soil_type__iexact=soil_type, plant_type__iexact=plant_type
            )

            recommendations = [plant.plant_name for plant in matching_plants]

            return render(
                request,
                "recommendation/mobile-app-recommendation.html",
                {"recommendations": recommendations},
            )

    return render(
        request, "recommendation/mobile-get-recommendation.html", {"form": form}
    )


def plat_details(request, plant_id):
    plant = get_object_or_404(Plant, id=plant_id)

    return render(request, "recommendation/plant-details.html", {"plant": plant})

