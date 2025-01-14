from django.urls import path
from . import views

app_name = "retailapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("testing", views.redshift_testing),
    path("search_result/", views.search_result, name="search_result"),
    path("weather_trend/", views.weather_trend, name="weather_trend"),
    path("snap_user/", views.weather_trend, name="snap_user"),
    path("snap_brand/", views.weather_trend, name="snap_brand"),
    path("get-small-category", views.get_small_category, name="get_small_category"),
]
