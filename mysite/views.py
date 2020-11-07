
from django.shortcuts import render
from django.shortcuts import render
from mysite.models import PlayList, video
from django.http import HttpResponse
from django.http import JsonResponse
import datetime
import random

# Create your views here.
def index(request):
    lucky_no = random.randint(1,49)
    numbers = list()
    for i in range(6):
        numbers.append(random.randint(1,49))
    #return HttpResponse("<h1>你今天的幸運號碼是:{}</h1>".format(lucky_no))
    return render ( request, "index.html", locals())

def date(request):
    return JsonResponse({'date':datetime.datetime.now()})

def playlist(request):
    items = PlayList.objects.all()
    return render(request, "playlist.html" , locals())

def showlist(request, id):
    titles = video.objects.filter(plist=id)
    return render(request, "showlist.html", locals())
