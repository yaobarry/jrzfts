from django.shortcuts import render,render_to_response
from gqs.models import PayList,SubPayList,CardBin

# Create your views here.

def homeview(request):
    return render_to_response('index.html')

