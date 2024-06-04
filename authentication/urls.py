from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import activate


urlpatterns = [
    path("", views.home, name="home"),
    path("signup", views.signup, name="signup"),
    path("signin", views.signin, name="signin"),
    path("signout", views.signout, name="signout"),
    path("about/", views.about, name="about"),
    path("team/", views.team, name="team"),
    path("blog/", views.blog, name="blog"),
    path("services/", views.services, name="services"),
    path("products/", views.products, name="products"),
    path("post-read/<int:post_id>/", views.post_read, name="post-read"),
    path("activate/<uidb64>/<token>", views.activate, name="activate"),
    path("forget-password", views.ForgetPassword, name="forget_password"),
    path("change-password/<token>/", views.ChangePassword, name="change_password"),
    path("flower", views.flower, name="flower"),
    path("vegetable", views.vegetable, name="vegetable"),
    path("herb", views.herb, name="herb"),
    path("shurb", views.shurb, name="shurb"),
    path("fruit", views.fruit, name="fruit"),
    path("climbing", views.climbing, name="climbing"),
    path("modern", views.modern, name="modern"),
    path("formal", views.formal, name="formal"),
    path("rock", views.rock, name="rock"),
    path("japan", views.japan, name="japan"),
    path("city", views.city, name="city"),
    path("trad", views.trad, name="trad"),
    path("tips", views.tips, name="tips"),
    path("care", views.care, name="care"),
    path("disease", views.disease, name="disease"),
    path("checkout/", views.checkout, name="checkout"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
