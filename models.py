# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

# Unable to inspect table 'ably_product_review_detail_tb'
# The error was: list index out of range

from django.contrib import admin
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ("title", "cat_depth4", "view_count", "like_count")
    search_fields = ("title", "cat_depth4")


class AuthGroup(models.Model):
    name = models.CharField(unique=True)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField()
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField()

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField()
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True)
    first_name = models.CharField()
    last_name = models.CharField()
    email = models.CharField()
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_login = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


# Unable to inspect table 'cm29_product_review_detail_tb'
# The error was: list index out of range


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.CharField(blank=True, null=True)
    object_repr = models.CharField()
    action_flag = models.SmallIntegerField()
    change_message = models.CharField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField()
    model = models.CharField()

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField()
    name = models.CharField()
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True)
    session_data = models.CharField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class MasterCategoryTb(models.Model):
    master_category_id = models.AutoField(primary_key=True)
    master_category_name = models.CharField()
    cat_depth_1 = models.CharField()
    cat_depth_2 = models.CharField()
    cat_depth_3 = models.CharField()

    class Meta:
        managed = False
        db_table = "master_category_tb"


# Unable to inspect table 'musinsa_product_review_detail_tb'
# The error was: list index out of range


class MusinsaSnapBrandRankingTb(models.Model):
    brand_id = models.CharField(primary_key=True)
    brand_name = models.CharField()
    img_url = models.CharField(blank=True, null=True)
    content_type = models.CharField()
    rank = models.IntegerField()
    previous_rank = models.IntegerField()
    follower_count = models.IntegerField()
    label_names = models.TextField()  # This field type is a guess.
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = "musinsa_snap_brand_ranking_tb"


class MusinsaSnapUserRankingTb(models.Model):
    story_id = models.CharField(primary_key=True)
    content_type = models.CharField()
    aggregation_like_count = models.IntegerField()
    tags = models.TextField()  # This field type is a guess.
    created_at = models.DateField()
    gender = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "musinsa_snap_user_ranking_tb"


class NaverShoppingKwdTb(models.Model):
    trend_id = models.AutoField(primary_key=True)
    start_date = models.DateField()
    end_date = models.DateField()
    time_unit = models.CharField()
    category_name = models.CharField()
    category_code = models.CharField()
    keyword_name = models.CharField()
    period = models.DateField()
    ratio = models.FloatField()
    created_at = models.DateField()
    gender = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "naver_shopping_kwd_tb"


# Unable to inspect table 'product_detail_tb'
# The error was: list index out of range
# Unable to inspect table 'ranking_tb'
# The error was: list index out of range


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
        managed = True  # Django가 테이블을 관리하지 않도록 설정


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


class SubCategoryTb(models.Model):
    sub_category_id = models.AutoField(primary_key=True)
    platform = models.CharField()
    master_category_id = models.IntegerField()
    cat_depth_4 = models.CharField()
    code = models.IntegerField(blank=True, null=True)
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = "sub_category_tb"


class TestTable(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "test_table"


class WeatherCenterLocationTb(models.Model):
    stn_id = models.IntegerField(primary_key=True)
    stn_ko = models.CharField()

    class Meta:
        managed = False
        db_table = "weather_center_location_tb"


class WeatherDailyTb(models.Model):
    stn = models.IntegerField(
        primary_key=True
    )  # The composite primary key (stn, tm) found, that is not supported. The first column is selected.
    tm = models.DateField()
    ws_avg = models.FloatField(blank=True, null=True)
    ws_max = models.FloatField(blank=True, null=True)
    ta_avg = models.FloatField(blank=True, null=True)
    ta_max = models.FloatField(blank=True, null=True)
    ta_min = models.FloatField(blank=True, null=True)
    hm_avg = models.FloatField(blank=True, null=True)
    hm_min = models.FloatField(blank=True, null=True)
    fg_dur = models.FloatField(blank=True, null=True)
    ca_tot = models.FloatField(blank=True, null=True)
    rn_day = models.FloatField(blank=True, null=True)
    rn_dur = models.FloatField(blank=True, null=True)
    rn_60m_max = models.FloatField(blank=True, null=True)
    rn_pow_max = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "weather_daily_tb"
        unique_together = (("stn", "tm"),)


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


class YoutubeVideoTb(models.Model):
    video_id = models.CharField(primary_key=True)
    gender = models.CharField(blank=True, null=True)
    category_name = models.CharField()
    channel_title = models.CharField()
    title = models.CharField()
    img_url = models.CharField()
    duration_seconds = models.IntegerField()
    published_at = models.DateTimeField()
    view_count = models.IntegerField()
    like_count = models.IntegerField(blank=True, null=True)
    created_at = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "'retail_gold_layer'.'youtube_gold_data'"


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
        verbose_name = "Video"
        verbose_name_plural = "Videos"
        managed = False
        unique_together = ()
