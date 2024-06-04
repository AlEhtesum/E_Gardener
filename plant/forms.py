from django import forms

class RecommendationForm(forms.Form):
    SEASON_CHOICES = [
        ('summer', 'Summer'),
        ('rainy', 'Rainy'),
        ('autumn', 'Autumn'),
        ('winter', 'Winter'),
        ('spring', 'Spring'),
    ]

    SOIL_TYPE_CHOICES = [
        ('clay', 'Clay'),
        ('loamy', 'Loamy'),
        ('sandy', 'Sandy'),
        ('sandy loam', 'Sandy loam'),
        ('clay loamy', 'Clay loamy'),
    ]
    PLANT_TYPE_CHOICES = [
         ('vegetable', 'Vegetable'),
        ('fruit', 'Fruit'),
        ('flower', 'Flower'),
        ('herbs', 'Herbs'),
        ('shurb', 'Shurb'),
         ('herbs', 'Herbs'),
        ('flowering shurb', 'Flowering Shurb'),
    ]
    SUNLIGHT_TYPE_CHOICES = [
        ('Full sun', 'Full Sun'),
        ('Partial sun', 'Partial Sun'),
        ]
    WATERING_TYPE_CHOICES = [
        ('Regular', 'Regular'),
        ('Occasional', 'Occasional'),
        ]

    season = forms.ChoiceField(choices=SEASON_CHOICES, label="Season of Interest")
    soil_type = forms.ChoiceField(choices=SOIL_TYPE_CHOICES, label="Soil Type")
    plant_type = forms.ChoiceField(choices=PLANT_TYPE_CHOICES,label="Plant Type")
    sunlight_type = forms.ChoiceField(choices=SUNLIGHT_TYPE_CHOICES, label="Sunlight")
    watering = forms.ChoiceField(choices=WATERING_TYPE_CHOICES , label="Water Need")