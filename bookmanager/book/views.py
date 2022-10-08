from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("ok")
    contex={
        "title":"Success，hello Django-Templates"
    }

    return render(request,"Book/index.html",context=contex)
