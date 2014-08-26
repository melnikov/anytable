# coding=utf-8
from django.shortcuts import *
from django.template import *
from anytable_v1.models import *
from django.contrib.auth import *
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import geocoder
import datetime
# Create your views here.

def index(request):
    events = Event.objects.all()
    cities = City.objects.all()
    types = VenueType.objects.all()
    venues = Venue.objects.all()
    kitchens = VenueKitchen.objects.all()
    options = VenueOptions.objects.all()
    date_today = datetime.date.today()

   # g = geocoder.ip('91.144.186.27')
    #g = g.city
    context = Context({"events":events, "cities":cities, "types": types, "venues":venues, "kitchens":kitchens, "options": options, "date_today": date_today,})

    return render_to_response('index.html', context)

def test(request):
    users = TestUsers.objects.all()
    admin = TestUsers.objects.get(pk= 2)
    events = Event.objects.all()
    venues = Venue.objects.all()
    context = Context({"users":users, "a":admin, "events":events, "v":venues})

    return render_to_response('test.html',context)


def ajaxFront(request, type):

    type = type.strip("/")
    if type == "0":
        venues = Venue.objects.all()
    else:
        venues = Venue.objects.filter(type = type)

    context = Context({"venues":venues, "request":request,})
    return render_to_response('ajaxFront.html', context)

def venueCard(request, id):
    id = int(id)
    if id > 0:
        svenue = Venue.objects.get(pk = id)
        latitude =  Geocoder.geocode(svenue.address)
        latitude = latitude[0].coordinates
        latitude = list(latitude)
        #sevents = event.objects.filter(venue__pk = id).order_by('-date')[:4]
        sevents = Event.objects.filter(venue__pk = id).order_by('-date')
        svenueimages = Venueimage.objects.filter(venue__pk = id)
        kitchens = VenueKitchen.objects.filter(venue__pk = id)
        #svenueimage = venueimage.objects.filter(venue__pk = id)
        context = Context({"venue":svenue, "events":sevents,"request":request, "venueimages":svenueimages, "kitchens":kitchens, "latitude":latitude})
        return render_to_response('venueCard.html', context)
    else:
        return render_to_response('badRequest.html',)

def redirect(url):

    HttpResponseRedirect(url)

@csrf_exempt
def searchResult(request):

    if request.method == "POST":
        city = request.POST['city']

        date = request.POST['date']

        if date:
            date = datetime.datetime.strptime(date, "%d-%m-%Y")
        else:
             date = datetime.date.today()


        type = request.POST['type']
        kitchen = request.POST['kitchen']
        options = request.POST.getlist('options')

        q1 = Venue.objects.all()
        search_q = ''
        if city :
            city_q = City.objects.get(pk = city)
            search_q = ('City: %s' % city_q.name)
            q1 = Venue.objects.filter(city__pk = city)
        if type:
            type_q = VenueType.objects.get(pk = type)
            search_q = search_q + (' | Type: %s' %type_q.name)
            q1 = q1.filter(type__pk = type)
        if kitchen:
            kitchen_q = VenueKitchen.objects.get(pk = kitchen)
            search_q = search_q + (' | Kitchen: %s' %kitchen_q.name)
            q1 = q1.filter(kitchen__pk = kitchen )
        if options :
            if len(options) > 1:
                options_q = VenueOptions.objects.filter(pk__in = options)
                #options_q = str(options_q)
                search_q = search_q + (' | Options: ')
                for option_q in options_q:
                    search_q = search_q + (' %s, ' % option_q.name)
            else:
                options_q = VenueOptions.objects.get(pk__in = options)
                search_q = search_q + (' | Options: %s' % options_q.name)
            q1 = q1.filter(option__pk__in = options ).distinct()

        q2 = Event.objects.filter(venue = q1 , event_date = date)
        #none_message = ''
        if q2.count() > 0 and q1.count() > 0:
            message = 'suggestion of venues matched the search, with no registered events, but here are Places matched ur search!'
            return render_to_response('searchResult.html', context_instance = RequestContext(request, {'search_q': search_q, 'venues':q1, 'events':q2,'city':city, 'message':message, 'date':date}))
        elif q2.count() == 0 and q1.count() > 0:
            date_s = datetime.datetime.strptime(str(date), '%Y-%m-%d').strftime('%d-%m-%Y')
            message = ('No events found on %s, but here are Places matched ur search!' % date_s )
            return render_to_response('searchResult.html', context_instance = RequestContext(request, {'search_q': search_q, 'venues':q1, 'city':city, 'message':message, 'date':date}))
        else:
            message = 'neither venues nor events matched ur search'
            return render_to_response('searchResult.html', context_instance = RequestContext(request, { 'search_q': search_q, 'events':q2, 'city':city, 'message':message}))



    else:
        return render_to_response('badRequest.html',)

    #context_instance = RequestContext(request, {"v":v})
    #else:
        #ana = 'idk'
        #return render_to_response('searchResult.html', context_instance = RequestContext(request, {'a':ana,}))



