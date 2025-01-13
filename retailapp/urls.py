from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("testing", views.redshift_testing),
    path("search_result/", views.search_result, name="search_result"),
    path("api/get-small-category", views.get_small_category, name="get_small_category"),
]
