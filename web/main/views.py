from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(response):
    return render(response, "main/base.html", {})



def v1(response):
    return render(response, "main/krtek.html", {"jmeno" : "krtek",
                                                "text" : "krtek je cerny slepy zvire, ktery hrabe hrabe..."})

