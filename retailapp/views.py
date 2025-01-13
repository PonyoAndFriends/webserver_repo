from django.db import connections
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from retailapp.models import ProductDetail

def index(request):
    return render(request, "index.html")  # 프로젝트 수준의 templates/index.html


def redshift_testing(request):
    with connections['redshift'].cursor() as cursor:
        cursor.execute("SELECT * FROM retail_silver_layer.ranking_tb")
        result = cursor.fetchall()
    return HttpResponse(f'Redshift Result: {result[0]}')


def detail(request):
    return render(request, "retailapp/detail.html")  # 앱 수준의 templates/retailapp/detail.html

def weather_trend(request):
    return render(request, 'retailapp/weather_trend.html')

'''
def list_dashboards(request):
    dashboards = SupersetDashboard.objects.all().values('id', 'dashboard_title', 'slug')
    return HttpResponse(list(dashboards), content_type="application/json")
'''
def search_result(request):
    products = ProductDetail.objects.all()
    # products = Product.objects.all()

    return render(request, 'retailapp/search_result.html', {'products': products})

def superset_dashboard(request):
    return render(request, 'superset_dashboard.html')

def get_small_category(request):
    gender = request.GET.get('gender', '')
    large_category = request.GET.get('largeCategory', '')
    middle_category = request.GET.get('middleCategory', '')
    platform = request.GET.get('platform', '')
    # 디버깅: 파라미터 확인
    print("Gender:", gender)
    print("Large Category:", large_category)
    print("Middle Category:", middle_category)
    print("Platform:", platform)


    query = """
        SELECT DISTINCT small_category_name
        FROM retail_silver_layer.product_detail_tb
        WHERE master_category_name = %s
        AND platform = %s
    """
    master_category = f'{gender}-{large_category}-{middle_category}'
    print("요거 출력 : ", master_category)
    with connections.cursor() as cursor:
        cursor.execute(query, [master_category, platform])
        rows = cursor.fetchall()

    small_categories = [row[0] for row in rows]
    return JsonResponse(small_categories, safe=False)