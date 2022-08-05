from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def debit_message(request):
    return HttpResponse("hi,your account has been debited as 1000")
def credit_message(request):
    return HttpResponse("Hi,your account has been credited as 1000")
