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

def save_file(file, path='images/'):

    filename = file.name
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()
@csrf_exempt
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        if len(name) == 0:
            return HttpResponse('name', mimetype='text/plain')
        elif len(email) == 0:
            return HttpResponse('email', mimetype='text/plain')
        elif len(pwd) == 0:
            return HttpResponse('pwd', mimetype='text/plain')
        else:
            #pwd = '123'
            new_account = Customer.objects.create(name = name, email = email, password= pwd)
            #new_account.save()
            request.session['customer_id']= new_account.id
            return HttpResponse("done", mimetype='text/plain')
    else:
        return render_to_response('badRequest.html', )


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
        try:
            customer_id = request.session['customer_id']
            customer = Customer.objects.get(pk = customer_id)
            context = Context({"customer":customer, })
            return render_to_response('private/cusProfile.html', context)
        except :
            return render_to_response('badRequest.html', )

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

@csrf_exempt
def cusImg(request):
    if request.method == 'POST':
        file = request.FILES
        if file:
            save_file(request.FILES['cusImg'])
            the_file = ('images/%s' % request.FILES['cusImg'])
            customer = Customer.objects.get(pk = request.session['customer_id'])
            customer.image = the_file
            message = customer.image.name
            customer.save()

            return HttpResponse(message, mimetype='text/plain')

@csrf_exempt
def cusPhone(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        customer = Customer.objects.get(pk = request.session['customer_id'])
        customer.phone = phone
        customer.save()

        return HttpResponse(phone, mimetype='text/plain')

@csrf_exempt
def cusEmail(request):
    if request.method == 'POST':
        email = request.POST['email']
        email = email.lower()
        customer = Customer.objects.get(pk = request.session['customer_id'])
        customer.email = email
        customer.save()
        return HttpResponse(email, mimetype='text/plain')

@csrf_exempt
def cusFacebook(request):
    if request.method == 'POST':
        fb = request.POST['facebook']
        customer = Customer.objects.get(pk = request.session['customer_id'])
        customer.facebook = fb
        customer.save()
        return HttpResponse(fb, mimetype='text/plain')

@csrf_exempt
def cusInstagram(request):
    if request.method == 'POST':
        instagram = request.POST['instagram']
        customer = Customer.objects.get(pk = request.session['customer_id'])
        customer.instagram = instagram
        customer.save()
        return HttpResponse(instagram, mimetype='text/plain')

@csrf_exempt
def cusTwitter(request):
    if request.method == 'POST':
        twitter = request.POST['twitter']
        customer = Customer.objects.get(pk = request.session['customer_id'])
        customer.twitter = twitter
        customer.save()
        return HttpResponse(twitter, mimetype='text/plain')

@csrf_exempt
def cusVk(request):
    if request.method == 'POST':
        vk = request.POST['vk']
        customer = Customer.objects.get(pk = request.session['customer_id'])
        customer.vk = vk
        customer.save()
        return HttpResponse(vk, mimetype='text/plain')

@csrf_exempt
def cuslogOut(request):
    try:
        del request.session['customer_id']
        #del request.session['logged_in']
        #del request.session['user_is']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")