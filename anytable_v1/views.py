# coding=utf-8
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import Context
from anytable_v1.models import *

def index(request):
    events = event.objects.all()
    cities = city.objects.all()
    types = venueType.objects.all()
    venues = venue.objects.all()
    kitchens = venueKitchen.objects.all()

    context = Context({"events":events, "cities":cities, "types": types, "venues":venues, "kitchens":kitchens,})

    return render_to_response('index.html', context)

def test(request):
    users = testUsers.objects.all()
    admin = testUsers.objects.get(pk= 2)
    events = event.objects.all()
    venues = venue.objects.all()
    context = Context({"users":users, "a":admin, "events":events, "v":venues})

    return render_to_response('test.html',context)


def ajaxFront(request, type):

    type = type.strip("/")
    venues = venue.objects.filter(type = type)

    context = Context({"venues":venues, "request":request,})
    return render_to_response('ajaxFront.html', context)


def venueCard(request, id):

    svenue = venue.objects.get(pk = id)
    sevents = event.objects.filter(venue__pk = id).order_by('-date')[:4]
    svenueimages = venueimage.objects.filter(venue__pk = id)
    kitchens = venueKitchen.objects.filter(venue__pk = id)
    #svenueimage = venueimage.objects.filter(venue__pk = id)
    context = Context({"venue":svenue, "events":sevents,"request":request, "venueimages":svenueimages, "kitchens":kitchens})
    return render_to_response('venueCard.html', context)