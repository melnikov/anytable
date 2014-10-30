# coding=utf-8
from django.shortcuts import *
from django.template import *
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from .forms.private_forms import *
from anytable_v1.models import *
from anytable.settings import *
from imagekit.admin import AdminThumbnail
import datetime
import _md5
import hashlib
from django.contrib.auth import authenticate, login


@csrf_exempt
def register(request):
    name = request.POST['name']
    email = request.POST['email']
    pwd = request.POST['pwd']
    #pwd = '123'
    new_account = Customer.objects.create(name = name, email = email, password= pwd)
    #new_account.save()
    request.session['customer_id']= new_account.id

    return HttpResponse("done")

@csrf_exempt
def login(request):
    email = request.POST['email']
    pwd = request.POST['pwd']
    pwd = computeMD5hash(pwd)
    customer = Customer.objects.get(email = email, password = pwd)
    if customer:
        request.session['customer_id']= customer.id
        return HttpResponse("done")
    else:
        return HttpResponse('user doesn\'t exist')

def profile(request):

        customer_id = request.session['customer_id']
        customer = Customer.objects.get(pk = customer_id)

        context = Context({"customer":customer, })

        return render_to_response('private/customerProfile.html', context)



@csrf_exempt
def customer_auth(request):
    if request.method == 'POST':
        email = request.POST['email']
        email = email.lower()
        password = request.POST['pwd']
        password = computeMD5hash(password)
       #try:
        the_customer = Customer.objects.get(email = email, password = password)

        #if customer is not None:
        #return HttpResponse('done', mimetype='text/plain')
        #else:
        return HttpResponse(email, mimetype='text/plain')