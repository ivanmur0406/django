from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "main/penguin_home.html")
def door(request):
    return render(request, "main/penguin_big.html")
