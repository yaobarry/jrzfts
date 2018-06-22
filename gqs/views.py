from django.shortcuts import render,render_to_response
from gqs.models import PayList,SubPayList,CardBin
from gqs.form import PayWayForm,CardNoForm,CardBinForm

# Create your views here.

def homeview(request):
    return render_to_response('index.html')

def paywaylist(request):
    if request.method == 'POST':
        form = PayWayForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            payway_list = list(filter(lambda x: x.pid == x.pid & int(cd['payway']), PayList.objects.filter(status=1)))
            subpayway_list = list(filter(lambda x: x.sid == x.sid & int(cd['subpayway']), SubPayList.objects.filter(status=1)))
            return render_to_response('payway.html',{'form':form,'payway_list':payway_list,'subpayway_list':subpayway_list})
    else: form = PayWayForm()
    return render_to_response('payway.html',{'form':form,})

def cardnocheck(request):
    if request.method == 'POST':
        form = CardNoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cn = str(cd['cardno'])
            sumj=0
            sumo=0
            for i in range(1,len(cn)+1):
                if i%2==0:
                    if int(cn[-i])*2>9:
                        sumo=sumo+int(cn[-i])*2-9
                    else: sumo=sumo+int(cn[-i])*2
                else:sumj=sumj+int(cn[-i])
            if (sumj+sumo)%10==0:
                return render_to_response('cardno.html',{'form':form,'result':'卡号符合Luhn规则！'})
            else:
                return render_to_response('cardno.html', {'form': form, 'result': '卡号不符合Luhn规则，请检查卡号！'})
    else: form = CardNoForm()
    return  render_to_response('cardno.html',{'form':form})

def cardbinquery(request):
    if request.method == 'POST':
        form = CardBinForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cb = CardBin.objects.filter(cardbin = cd['cardbin'])
            if not cb:
                error='暂无此卡bin数据！'
                return render_to_response('cardbin.html',{'form':form,'error':error })
            else:
                return render_to_response('cardbin.html', {'form': form, 'cb': cb})
    else: form = CardBinForm()
    return  render_to_response('cardbin.html',{'form':form})