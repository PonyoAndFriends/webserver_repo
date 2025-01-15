from django.db import connections
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from retailapp.models import ProductDetail
from django.db.models import Q
from django.core.cache import cache
from retailapp.models import Video


def video_list(request):

    query = request.GET.get("q")  # 검색창 입력값 가져오기
    if query:
        videos = Video.objects.filter(
            title__icontains=query
        )  # 제목에 검색어 포함된 데이터 필터링
        videosqq = Video.objects.filter(title__icontains=query).query
        print(videosqq)
    else:
        videos = Video.objects.all()  # 검색어 없으면 모든 데이터 가져오기
        videosq = Video.objects.all().query
        print(videosq)

    return render(
        request, "retailapp/snap_brand.html", {"videos": videos, "query": query}
    )


def index(request):
    return render(request, "index.html")  # 프로젝트 수준의 templates/index.html


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


def snap_brand(request):
    return render(request, "retailapp/snap_brand.html")


def snap_user(request):
    return render(request, "retailapp/snap_user.html")


"""
def list_dashboards(request):
    dashboards = SupersetDashboard.objects.all().values('id', 'dashboard_title', 'slug')
    return HttpResponse(list(dashboards), content_type="application/json")
"""

"""
def search_result(request):
    products = ProductDetail.objects.all().order_by('plarform')
    # products = Product.objects.all()
    return render(request, "retailapp/search_result.html", {"products": products})
"""


def search_result(request):
    # GET 파라미터 받기
    query = request.GET.get("query", "").strip()
    platform = request.GET.get("platform", "").strip()
    gender = request.GET.get("gender", "").strip()
    master_category = request.GET.get("master_category", "").strip()
    middle_category = request.GET.get("middle_category", "").strip()
    small_category = request.GET.get("small_category", "").strip()

    # 전체 데이터 가져오기
    products = ProductDetail.objects.all().order_by("ranking")

    # 필터 조건 적용
    if platform:
        products = products.filter(platform=platform)
    if gender:
        products = products.filter(cat_depth_1=gender)
    if master_category:
        products = products.filter(cat_depth_2=master_category)
    if middle_category:
        products = products.filter(cat_depth_3=middle_category)
    if small_category:
        products = products.filter(small_category_name=small_category)
    if query:
        products = products.filter(
            Q(product_name__icontains=query) | Q(brand_name_kr__icontains=query)
        )
    # 결과를 컨텍스트에 담아 렌더링
    context = {
        "products": products,
        "query": query,
        "platform": platform,
        "gender": gender,
        "master_category": master_category,
        "middle_category": middle_category,
        "small_category": small_category,
    }

    return render(request, "retailapp/search_result.html", context)


def item_detail(request, product_id):
    product = get_object_or_404(ProductDetail, pk=product_id)
    reviews = (
        product.reviews.all()
    )  # related_name='reviews'를 사용해 연결된 리뷰를 가져옴

    # 리뷰 데이터를 리스트로 변환
    reviews_data = [
        {
            "reviewer_name": review.reviewer_name,
            "rating": review.rating,
            "comment": review.comment,
            "created_at": review.created_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
        for review in reviews
    ]

    return JsonResponse(
        {
            "product_id": product.product_id,
            "product_name": product.product_name,
            "price": float(product.price),
            "description": product.description,
            "image_url": product.image.url,
            "reviews": reviews_data,
        }
    )


def get_product_reviews_with_cache(request):
    product_id = request.GET.get("product_id")  # 프론트에서 전달된 product_id

    if not product_id:
        return JsonResponse({"error": "Missing productId"}, status=400)

    # 캐시 키 생성
    cache_key = f"product_reviews_{product_id}"

    # 1. 캐시 확인
    cached_data = cache.get(cache_key)
    if cached_data:
        # 캐시된 데이터 반환
        return JsonResponse(cached_data, safe=False)

    # 2. 캐시에 데이터가 없으면 Redshift에서 데이터 조회
    review_tables = [
        '"retail_silver_layer"."musinsa_product_review_detail_tb"',
        '"retail_silver_layer"."cm29_product_review_detail_tb"',
        '"retail_silver_layer"."ably_product_review_detail_tb"',
    ]  # 세 플랫폼 테이블
    all_reviews = []

    for table in review_tables:
        # "."로 분리하고 두 번째 부분에서 "musinsa" 추출
        platform_name = table.split(".")[1].split("_")[0].strip('"')
        if platform_name == "cm29":
            platform_name = "29CM"

        query = f"""
            SELECT *
            FROM {table}
            WHERE product_id = %s
            ORDER BY review_date DESC;  -- 날짜순 정렬
            """
        with connections["default"].cursor() as cursor:
            cursor.execute(query, [product_id])
            rows = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            all_reviews.extend(
                [{**dict(zip(columns, row)), "platform": platform_name} for row in rows]
            )

    # 캐시에 저장 (유효 시간: 300초)
    cache.set(cache_key, all_reviews, timeout=300)

    # 데이터 반환
    return JsonResponse(all_reviews, safe=False)


def superset_dashboard(request):
    return render(request, "superset_dashboard.html")


def weather_trend(request):
    return render(request, "retailapp/weather_trend.html")


def get_small_category(request):
    gender = request.GET.get("gender", "").strip()
    platform = request.GET.get("platform", "").strip()
    master_category = request.GET.get("master_category", "").strip()
    middle_category = request.GET.get("middle_category", "").strip()

    # 필수 조건이 하나라도 없다면 빈 배열 반환
    if not gender or not platform or not master_category or not middle_category:
        return JsonResponse([], safe=False)

    # ProductDetail 모델에서 소분류를 필터링
    small_categories = (
        ProductDetail.objects.filter(
            cat_depth_1=gender,  # 성별 필터링
            platform=platform,  # 플랫폼 필터링
            cat_depth_2=master_category,  # 대분류 필터링
            cat_depth_3=middle_category,  # 중분류 필터링
        )
        .values_list("small_category_name", flat=True)
        .distinct()
    )

    small_categories = list(small_categories)

    return JsonResponse(small_categories, safe=False)
