from django.urls import path
from . import views

app_name = "retailapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("detail/", views.detail, name="detail"),
    path("testing", views.redshift_testing),
    path("search_result/", views.search_result, name="search_result"),
    path("weather_trend/", views.weather_trend, name="weather_trend"),
    path("snap_user/", views.snap_user, name="snap_user"),
    path("snap_brand/", views.snap_brand, name="snap_brand"),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path("get-small-category", views.get_small_category, name="get_small_category"),
    path("search_result/get_product_reviews_with_cache/", views.get_product_reviews_with_cache, name="search_result/get_product_reviews_with_cache"),
    path('get-small-categories/', views.get_small_category, name='get_small_categories'),
    path('video-list/', views.video_list, name='video_list'),  # video_list URL 패턴 정의
    #path('search_videos/', views.search_videos, name='search_videos'),
]
