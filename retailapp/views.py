from django.db import connections
from django.shortcuts import render
from django.http import HttpResponse

def redshift_testing(request):
    with connections['redshift'].cursor() as cursor:
        cursor.execute("SELECT * FROM retail_silver_layer.ranking_tb")
        result = cursor.fetchall()
    return HttpResponse(f'Reedshift Result : {result[0]}')

# Create your views here.
def index(request):
    
    return HttpResponse("Hello, world. You're at the retailapp index.")