from django.db import models

# Create your models here.

class PayList(models.Model):
    pid = models.BigIntegerField()
    payname = models.CharField(max_length=100)
    status = models.BooleanField()
    def __str__(self):
        return self.payname

class SubPayList(models.Model):
    sid = models.BigIntegerField()
    subpayname = models.CharField(max_length=100)
    status = models.BooleanField()
    def __str__(self):
        return self.subpayname

class CardBin(models.Model):
    cardbin = models.CharField(max_length=10)
    cardnolen =  models.IntegerField()
    cardtype =  models.BooleanField()
    status = models.BooleanField()
    bankname = models.CharField(max_length=100)
    bankabbname = models.CharField(max_length=10)
    associations = models.CharField(max_length=100)
    country = models.CharField(max_length=10)
    def __str__(self):
        return self.cardbin


