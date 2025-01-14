from django.db import connections
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from retailapp.models import ProductDetail
from django.db.models import Q

def index(request):
    return render(request, "retailapp/index.html")  # 프로젝트 수준의 templates/index.html


def redshift_testing(request):
    with connections["redshift"].cursor() as cursor:
        cursor.execute("SELECT * FROM retail_silver_layer.ranking_tb")
        result = cursor.fetchall()
    return HttpResponse(f"Redshift Result: {result[0]}")


def detail(request):
    return render(
        request, "retailapp/detail.html"
    )  # 앱 수준의 templates/retailapp/detail.html


def weather_trend(request):
    return render(request, "retailapp/weather_trend.html")


"""
def list_dashboards(request):
    dashboards = SupersetDashboard.objects.all().values('id', 'dashboard_title', 'slug')
    return HttpResponse(list(dashboards), content_type="application/json")
"""

'''
def search_result(request):
    products = ProductDetail.objects.all().order_by('plarform')
    # products = Product.objects.all()
    return render(request, "retailapp/search_result.html", {"products": products})
'''

def search_result(request):
    query = request.GET.get('query', '').strip()
    platform = request.GET.get('platform', '').strip()
    gender = request.GET.get('gender', '').strip()
    master_category = request.GET.get('master_category', '').strip()
    small_category = request.GET.get('small_category', '').strip()

    products = ProductDetail.objects.all()

    # 필터링 옵션 적용
    if platform:
        products = products.filter(platform=platform)
    if master_category:
        products = products.filter(master_category_name=master_category)
    if small_category:
        products = products.filter(small_category_name=small_category)

    # 검색어 필터링
    if query:
        products = products.filter(
            Q(platform__icontains=query) |
            Q(master_category_name__icontains=query) |
            Q(small_category_name__icontains=query) |
            Q(product_name__icontains=query) |
            Q(brand_name_kr__icontains=query) |
            Q(brand_name_en__icontains=query)
        )
        # 검색어가 있을 때는 정렬을 기본 정렬 또는 다른 기준으로 설정할 수 있습니다.
        # 여기서는 검색어가 있을 때도 platform으로 정렬합니다.
        products = products.order_by('platform')
    else:
        # 검색어가 없을 때는 platform으로 정렬
        products = products.order_by('platform')

    context = {
        'products': products,
        'query': query,
        'platform': platform,
        'master_category': master_category,
        'small_category': small_category,
    }

    return render(request, "retailapp/search_result.html", context)

def superset_dashboard(request):
    return render(request, "superset_dashboard.html")


def weather_trend(request):
    return render(request, "retailapp/weather_trend.html")


def get_small_category(request):
    master_category = request.GET.get('masterCategory', '').strip()

    if not master_category:
        return JsonResponse([], safe=False)

    # ProductDetail 모델에서 소분류를 추출
    small_categories = ProductDetail.objects.filter(
        master_category_name=master_category
    ).values_list('small_category_name', flat=True).distinct()

    small_categories = list(small_categories)

    return JsonResponse(small_categories, safe=False)