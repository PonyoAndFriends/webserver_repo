# Generated by Django 5.1.2 on 2025-01-14 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("retailapp", "0003_alter_productdetail_table"),
    ]

    operations = [
        migrations.CreateModel(
            name="SilverProductDetail",
            fields=[
                ("platform", models.CharField(max_length=100)),
                ("master_category_name", models.CharField(max_length=32)),
                ("small_category_name", models.CharField(max_length=50)),
                ("product_id", models.IntegerField(primary_key=True, serialize=False)),
                ("img_url", models.URLField(max_length=1000)),
                ("product_name", models.CharField(max_length=512)),
                ("brand_name_kr", models.CharField(max_length=100)),
                ("brand_name_en", models.CharField(max_length=100)),
                ("original_price", models.IntegerField()),
                ("final_price", models.IntegerField()),
                ("discount_ratio", models.IntegerField()),
                ("review_counting", models.IntegerField()),
                ("review_avg_rating", models.FloatField()),
                ("like_counting", models.IntegerField()),
                ("created_at", models.DateField()),
            ],
            options={
                "db_table": '"retail_silver_layer"."product_detail_tb"',
                "managed": False,
            },
        ),
        migrations.AlterModelTable(
            name="productdetail",
            table='"retail_gold_layer"."total_product_gold_tb"',
        ),
    ]
