from django.shortcuts import render

# Create your views here.
def home_page(requests):
    return render(requests, 'blog/home_page.html', {})