from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def sonu(request):
    return HttpResponse('<marquee><h2>thinavara raaa</marquee></h2>')

def hm(request):
    return HttpResponse('inka tinaledhu raa aaa')

def ff(request):
    return HttpResponse('podhamaaaaaaaaaaaa')