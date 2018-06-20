from django.shortcuts import render,render_to_response
from gqs.models import PayList,SubPayList,CardBin
from gqs.form import PayWayForm

# Create your views here.
def

def homeview(request):
    return render_to_response('index.html')

def paywaylist(request):
    if request.method == 'POST':
        form = PayWayForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            payway_list = PayList.objects.filter( pid = pid&cd.payway)
            subpayway_list = SubPayList.objects.filter(sid = sid&cd.subpayway)
            return render_to_response('payway.html',{'form':form,'payway_list':payway_list,'subpayway_list':subpayway_list})
    else: form = PayWayForm()
    return  render_to_response('payway.html','form':form)
