from django import forms

class PayWayForm(forms.Form):
    payway = forms.IntegerField()
    subpayway = forms.IntegerField()