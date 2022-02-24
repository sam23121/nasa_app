from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.
def index(request):
    response = requests.get('https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key=DEMO_KEY')
    jsonResponse = response.json()
    return render(request, 'blog/index.html', {'jsonResponse': jsonResponse})

def specific(request, article_id):
    return render(request, 'blog/index.html', {
        'article_id': article_id
    })