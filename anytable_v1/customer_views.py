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
    new_account = Customer.objects.create(name = name, email = email, password = pwd)
    new_account.save()
    try:
        return HttpResponse('success!')

    except KeyError:
        pass
    return HttpResponse("something went wrong!")

def profile(request):
    return render_to_response('private/customerProfile.html',)