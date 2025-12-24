from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time
from .tasks import sendEmail
import requests
# Create your views here.

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")



@cache_page(60)
def test(request):
    response = requests.get("https://c393a699-bd6a-4c5c-b140-f435b616bfa1.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())



@cache_page(60*20)
def weather_view(request,city):  
    response = requests.get("https://api.openweathermap.org/data/2.5/weather",params = {
        "q": city,
        "appid": "399871d262777e04375a1aea5f67f442",
        "units": "metric",
        "lang": "fa"
        },timeout=5)
    return JsonResponse(response.json())
   
    
