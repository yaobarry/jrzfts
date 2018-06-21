from django.shortcuts import render,render_to_response
from gqs.models import PayList,SubPayList,CardBin
from gqs.form import PayWayForm,CardNoForm

# Create your views here.

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
    return  render_to_response('payway.html',{'form':form})

def cardnocheck(request):
    if request.method == 'POST':
        form = CardNoForm(request.POST)
        if form.is_valid():
            cn = str(form.cardno)
            for i in range(1,len(cn)+1):
                if i%2==0:
                    if int(cn[i])*2>9:
                        sumo=sumo+int(cn[i])*2-9
                    else: sumo=sumo+int(cn[i])*2
                else:sumj=sumj+int(cn[i])
                isok=(sumj+sumo)%10
            if isok==0:
                return render_to_response('cardno.html',{'form':form,'result':'卡号符合Luhn规则！'})
            else:
                return render_to_response('cardno.html', {'form': form, 'result': '卡号不符合Luhn规则，请检查卡号！'})
    else: form = CardNoForm()
    return  render_to_response('cardno.html',{'form':form})
