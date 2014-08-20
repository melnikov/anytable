# coding=utf-8
from django.shortcuts import *
from django.template import *
from anytable_v1.models import *
from django.contrib.auth import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect


from django.core.context_processors import csrf
# Create your views here.

def index(request):
    events = event.objects.all()
    cities = city.objects.all()
    types = venueType.objects.all()
    venues = venue.objects.all()
    kitchens = venueKitchen.objects.all()
    options = venueOptions.objects.all()

    context = Context({"events":events, "cities":cities, "types": types, "venues":venues, "kitchens":kitchens, "options": options,})

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
    if type == "0":
        venues = venue.objects.all()
    else:
        venues = venue.objects.filter(type = type)

    context = Context({"venues":venues, "request":request,})
    return render_to_response('ajaxFront.html', context)

def venueCard(request, id):

    svenue = venue.objects.get(pk = id)
    latitude =  Geocoder.geocode(svenue.address)
    latitude = latitude[0].coordinates
    latitude = list(latitude)
    #sevents = event.objects.filter(venue__pk = id).order_by('-date')[:4]
    sevents = event.objects.filter(venue__pk = id).order_by('-date')
    svenueimages = venueimage.objects.filter(venue__pk = id)

    kitchens = venueKitchen.objects.filter(venue__pk = id)
    #svenueimage = venueimage.objects.filter(venue__pk = id)
    context = Context({"venue":svenue, "events":sevents,"request":request, "venueimages":svenueimages, "kitchens":kitchens, "latitude":latitude})
    return render_to_response('venueCard.html', context)

@csrf_exempt
def searchResult(request):
    if request.method == "POST":

        #if request.POST['city'] > '0':
        #    var = 'activated'
        city = request.POST['city']
        type = request.POST['type']
        kitchen = request.POST['kitchen']
        options = request.POST.getlist('options')
        #options = list(options)
        q1 = venue.objects.all()
        if city :
            q1 = venue.objects.filter(city__pk = city)
        #q_city = venue.objects.filter(city__pk = city)
        if type:
            q1 = q1.filter(type__pk = type)
        if kitchen:
            q1 = q1.filter(kitchen__pk = kitchen)
        if options :
            q1 = q1.filter(option__pk__in = options).distinct()

        return render_to_response('searchResult.html', context_instance = RequestContext(request, {'venues':q1, 'city':city, }))
    #context_instance = RequestContext(request, {"v":v})
    #else:
        #ana = 'idk'
        #return render_to_response('searchResult.html', context_instance = RequestContext(request, {'a':ana,}))



