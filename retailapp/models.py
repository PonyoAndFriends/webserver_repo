from django.db import models


class Video(models.Model):
    id = models.CharField(max_length=20, unique=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    cat_depth2 = models.CharField(max_length=100, blank=True, null=True)
    cat_depth3 = models.CharField(max_length=100, blank=True, null=True)
    cat_depth4 = models.CharField(max_length=100, blank=True, null=True)
    channel_title = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    img_url = models.URLField(max_length=1000, blank=True, null=True)
    duration_seconds = models.IntegerField(blank=True, null=True)
    published_date = models.CharField(max_length=52, blank=True, null=True)
    view_count = models.IntegerField(blank=True, null=True)
    like_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)

    class Meta:
        db_table = '"retail_gold_layer"."youtube_gold_data"'
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
        managed=False
        unique_together = ()

class ProductDetail(models.Model):
    platform = models.CharField(max_length=100)  # varchar(100)
    cat_depth_1 = models.CharField(max_length=32)  # varchar(32)
    cat_depth_2 = models.CharField(max_length=32)  # varchar(32)
    cat_depth_3 = models.CharField(max_length=32)  # varchar(32)
    small_category_name = models.CharField(max_length=50)  # varchar(50)
    product_id = models.IntegerField(primary_key=True)  # int4 (Primary Key)
    product_name = models.CharField(max_length=512)  # varchar(512)
    ranking = models.IntegerField()  # int4
    img_url = models.URLField(max_length=1000)  # varchar(1000)
    brand_name_kr = models.CharField(max_length=100)  # varchar(100)
    original_price = models.IntegerField()  # int4
    final_price = models.IntegerField()  # int4
    discount_ratio = models.IntegerField()  # int4
    review_counting = models.IntegerField()  # int4
    review_avg_rating = models.FloatField()  # float8
    like_counting = models.IntegerField()  # int4
    created_at = models.DateField()  # date

    class Meta:
        db_table = '"retail_gold_layer"."total_product_gold_tb"'  # 테이블 이름
        managed = False  # Django가 테이블을 관리하지 않도록 설정

class SilverProductDetail(models.Model):
    platform = models.CharField(max_length=100)  # varchar(100)
    master_category_name = models.CharField(max_length=32)  # varchar(32)
    small_category_name = models.CharField(max_length=50)  # varchar(50)
    product_id = models.IntegerField(primary_key=True)  # int4 (Primary Key)
    img_url = models.URLField(max_length=1000)  # varchar(1000)
    product_name = models.CharField(max_length=512)  # varchar(512)
    brand_name_kr = models.CharField(max_length=100)  # varchar(100)
    brand_name_en = models.CharField(max_length=100)  # varchar(100)
    original_price = models.IntegerField()  # int4
    final_price = models.IntegerField()  # int4
    discount_ratio = models.IntegerField()  # int4
    review_counting = models.IntegerField()  # int4
    review_avg_rating = models.FloatField()  # float8
    like_counting = models.IntegerField()  # int4
    created_at = models.DateField()  # date

    class Meta:
        db_table = '"retail_silver_layer"."product_detail_tb"'  # 테이블 이름
        managed = False  # Django가 테이블을 관리하지 않도록 설정

from django.db import models

class Video(models.Model):
    video_id = models.CharField(max_length=20)
    gender = models.CharField(max_length=100)
    cat_depth2 = models.CharField(max_length=100)
    cat_depth3 = models.CharField(max_length=100)
    cat_depth4 = models.CharField(max_length=100)
    channel_title = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    img_url = models.CharField(max_length=1000)
    duration_seconds = models.IntegerField()
    published_date = models.CharField(max_length=52)
    view_count = models.IntegerField()
    like_count = models.IntegerField()
    created_at = models.DateField()

    class Meta:
        db_table = '"retail_gold_layer"."youtube_gold_data"'  # 테이블 이름
        managed = False  # Django가 테이블을 관리하지 않도록 설정

    def __str__(self):
        return f"{self.cat_depth4}"



class Item(models.Model):
    product_id = models.IntegerField()
    review_content = models.TextField(max_length=4000)
    review_rating = models.IntegerField()
    review_date = models.DateField()
    reviewer_height = models.FloatField(null=True, blank=True)
    reviewer_weight = models.FloatField(null=True, blank=True)
    selected_options = models.CharField(max_length=30, null=True, blank=True)
    created_at = models.DateField()

    def __str__(self):
        return f"Review {self.id} for Product {self.product_id}"

class SupersetDashboard(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        app_label = "retailapp"
