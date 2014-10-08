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
##############################################
################## Venues ####################
##############################################
@csrf_exempt
def ven_admin_logout(request):
    try:
        del request.session['ven_admin_id']
        del request.session['logged_in']
        del request.session['user_is']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

@csrf_exempt
def venueadministratorauth(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password = computeMD5hash(password)
        try:
            venue_admin = VenueAdministrator.objects.get(email = email, password = password)
            if venue_admin is not None:

                request.session['ven_admin_id']= venue_admin.id
                request.session['logged_in'] = True
                request.session['user_is'] = 'ven_admin'

                val = venue_admin.id


                return HttpResponse(val, mimetype='text/plain')
        except venue_admin.DoesNotExist:
            return None

def TheVenueAdministration(request):
         if  'ven_admin_id' in request.session:
            user = VenueAdministrator.objects.get( pk = request.session['ven_admin_id'] )

            venuetypes = VenueType.objects.filter(venue = user.venue)
            types = VenueType.objects.all()

            venuekitchens = VenueKitchen.objects.filter(venue = user.venue)
            kitchens = VenueKitchen.objects.all()

            venueoptions = VenueOptions.objects.filter(venue = user.venue)
            options = VenueOptions.objects.all()

            images = Venueimage.objects.filter(venue = user.venue)
            events = Event.objects.filter(venue = user.venue).order_by('-id')

            event_prices = EventPrice.objects.filter(event = events)
            prices = PriceType.objects.all()

            date = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
            date_today = datetime.date.today()



            ven_admin_logged_in = True

            context = Context({"user":user, "venuetypes":venuetypes, "types":types, "venuekitchens":venuekitchens, "kitchens":kitchens, "venueoptions":venueoptions, "options":options, "images":images, "events":events, "date_today": date_today, "ven_admin_logged_in":ven_admin_logged_in, "prices":prices, "event_prices":event_prices,})
            return render_to_response('private/profile.html',context)
         else:
             return render_to_response('badRequest.html',)

@csrf_exempt
def DeleteVenueImg(request, id):
    id = id.strip('/')
    q = Venueimage.objects.filter(pk = id)
    q = q.delete()

    return HttpResponse('done', mimetype="text/plain")


def save_file(file, path='images/'):

    filename = file.name
    fd = open('%s/%s' % (MEDIA_ROOT, str(path) + str(filename)), 'wb')
    for chunk in file.chunks():
        fd.write(chunk)
    fd.close()

@csrf_exempt
def venueaddimg(request):
    # Handle file upload
    if request.method == 'POST':
        #form = DocumentForm(request.POST, request.FILES)
        #if form.is_valid():
            #newdoc = Document(docfile = request.FILES['docfile'])
            #newdoc.save()
            file = request.FILES
            if file:
                #form = DocumentForm(request.POST, request.FILES)
                #if form.is_valid():
                save_file(request.FILES['fileupload'])

                #title = request.FILES['fileupload'].name
                venuepk = request.POST['venuepk']
                docfile = ('images/%s' % request.FILES['fileupload'])

                #else:
                   #title = request.POST['hidden']
            #else:
                #title = 'no files'
                venue = Venue.objects.get(pk = venuepk)
                r = Venueimage.objects.create(image= docfile, description='just new img', venue= venue)
                r.save()
                #r = Document(title= 'request is post and %s' % venuepk, docfile = docfile)
                #r.save()
    else:
        r = Document(title = 'request is not post')
        r.svae()
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form

    ##return render_to_response('list.html', {'documents': documents, 'form': form}, context_instance=RequestContext(request) )
    return HttpResponse('done', mimetype="text/plain")

    #return HttpResponse(returnMsg, mimetype="text/plain")

     #return render_to_response('private/profile.html',)
     #return render_to_response('admin/anytable_v1/venueadministrator', context_instance = RequestContext(request, {'message':message}))
    # use his for ajax return : return HttpResponse('done', mimetype="text/plain")

@csrf_exempt
def venueupdatelogo(request):
    # Handle file upload
    if request.method == 'POST':
            file = request.FILES
            if file:
                save_file(request.FILES['logoupload'])
                venuepk = request.POST['venuepk']
                docfile = ('images/%s' % request.FILES['logoupload'])
                venue = Venue.objects.get(pk = venuepk)
                venue.image = docfile
                #venue.thumbnail = venue.image
                venue.save()
                message = venue.image.name
    else:
        r = Document(title = 'request is not post')
        r.svae()
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def update_venue_telephone(request):
    if request.method == 'POST':
        venueid = request.POST['venue']
        telephone = request.POST['telephone']
        v = Venue.objects.get(pk = venueid)
        v.tel = telephone
        v.save()
        message = 'saved'

        return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def update_venue_email(request):
    if request.method == 'POST':
        venueid = request.POST['venue']
        email = request.POST['email']
        v = Venue.objects.get(pk = venueid)
        v.email = email
        v.save()
        message = 'saved'

        return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def updatevenuesite(request):
    if request.method == 'POST':
        venueid = request.POST['venue']
        website = request.POST['website']
        v = Venue.objects.get(pk = venueid)
        v.website = website
        v.save()
        message = 'saved'

        return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def updatevenuefb(request):
    if request.method == 'POST':
        venueid = request.POST['venue']
        facebook = request.POST['facebook']
        v = Venue.objects.get(pk = venueid)
        v.facebook_url = facebook
        v.save()
        message = 'saved'

        return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def updatevenuetwitter(request):
    if request.method == 'POST':
        venueid = request.POST['venue']
        twitter = request.POST['twitter']
        v = Venue.objects.get(pk = venueid)
        v.twitter = twitter
        v.save()
        message = 'saved'

        return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def updatevenueinstagram(request):
    if request.method == 'POST':
        venueid = request.POST['venue']
        instagram = request.POST['instagram']
        v = Venue.objects.get(pk = venueid)
        v.instagram = instagram
        v.save()
        message = 'saved'

        return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def updatevenuevk(request):
    if request.method == 'POST':
        venueid = request.POST['venue']
        vk = request.POST['vk']
        v = Venue.objects.get(pk = venueid)
        v.vk_url = vk
        v.save()
        message = 'saved'

        return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def updatevenuedescription(request):
    if request.method == 'POST':
        venueid = request.POST['venue']
        description = request.POST['description']
        v = Venue.objects.get(pk = venueid)
        v.description = description
        v.save()
        message = 'saved'

        return HttpResponse(message, mimetype="text/plain")

@csrf_exempt
def update_venue_options(request):
    if request.method == 'POST':
        venueid = request.POST['venueid']
        venue = Venue.objects.get(pk = venueid)
        option_id = request.POST['option_id']
        the_venue_options = VenueOptions.objects.filter(venue = venue)
        the_new_option = VenueOptions.objects.get(pk = option_id)
        if the_new_option not in the_venue_options:
            v = venue.option.add(the_new_option)
        else:
            v = venue.option.remove(the_new_option)

        return HttpResponse(the_new_option.id, mimetype='text/plain')
    else:
        return HttpResponse('request is not post', mimetype='text/plain')


@csrf_exempt
def update_venue_kitchen(request):
    if request.method == 'POST':
        venueid = request.POST['venueid']
        venue = Venue.objects.get(pk = venueid)
        the_venue_kitchens = VenueKitchen.objects.filter(venue = venue)
        kitchen_id = request.POST['kitchen_id']
        the_new_kitchen = VenueKitchen.objects.get(pk = kitchen_id)
        if the_new_kitchen not in the_venue_kitchens:
            v = venue.kitchen.add(the_new_kitchen)
        else:
            v = venue.kitchen.remove(the_new_kitchen)

        return HttpResponse(the_new_kitchen.id, mimetype='text/plain')
    else:
        return HttpResponse('request is not post', mimetype='text/plain')

@csrf_exempt
def update_venue_type(request):
    if request.method == 'POST':
        venueid = request.POST['venueid']
        venue = Venue.objects.get(pk = venueid)
        the_venue_types = VenueType.objects.filter(venue = venue)
        type_id = request.POST['type_id']
        the_new_type = VenueType.objects.get(pk = type_id)
        if the_new_type not in the_venue_types:
            v = venue.type.add(the_new_type)
        else:
            v = venue.type.remove(the_new_type)

        return HttpResponse(the_new_type.id, mimetype='text/plain')
    else:
        return HttpResponse('request is not post', mimetype='text/plain')

##############################################
################## Events ####################
##############################################
@csrf_exempt
def addevent(request):

    if request.method == 'POST':
        venuepk = request.POST['venuepk']
        the_venue = Venue.objects.get(pk = venuepk)
        the_date = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")

        file = request.FILES
        save_file(request.FILES['eventimg'])
        docfile = ('images/%s' % request.FILES['eventimg'])
        ev = Event.objects.create(title='title',venue = the_venue, date = the_date, image = docfile)
        ev.save()
        id= ev.id
        return HttpResponse(id, mimetype="text/plain")


@csrf_exempt
def delete_event(request):
    if request.method == 'POST':
        eventid = request.POST['eventid']
        event = Event.objects.get(pk = eventid)
        event = event.delete()
        return HttpResponse('done', mimetype="text/plain")

@csrf_exempt
def update_event(request):
    if request.method == 'POST':
        event_id = request.POST['eventid']
        ev = Event.objects.get(pk = event_id)

        event_title = request.POST['eventtitle']
        if event_title:
             ev.title = event_title
        event_description = request.POST['eventdescription']
        if event_description:
            ev.description = event_description
        event_date = request.POST['event_date']
        event_date = datetime.datetime.strptime(event_date, "%d-%m-%Y")
        if event_date:
            ev.event_date = event_date

        event_time = request.POST['event_time']
        event_time = datetime.datetime.strptime(event_time, "%H:%M")
        if event_time:
             ev.event_time = event_time

        ev.save()
        return HttpResponse('yep saved!', mimetype='text/plain')

@csrf_exempt
def update_event_img(request):
    if request.method == 'POST':
        eventid = request.POST['eventid']
        file = request.FILES
        input = 'updateeventimg_%s' % eventid
        save_file(request.FILES['updateeventimg'])
        docfile = ('images/%s' % request.FILES['updateeventimg'])
        ev = Event.objects.get(pk = eventid)
        ev.image = docfile
        ev.save()
        #message = request.FILES['updateeventimg'].name
        message = docfile
        return HttpResponse(message, mimetype='text/plain')

@csrf_exempt
def update_event_price(request):
    if request.method == 'POST':
        event_id = request.POST['event_id']
        price_type = request.POST['price_type']
        the_price = request.POST['the_price']

        the_event = Event.objects.get(pk = event_id)
        the_price_type = PriceType.objects.get(pk = price_type)

        event_price = EventPrice.objects.create(price_type = the_price_type, price = the_price, event = the_event)
        event_price.save()

        message = price_type
        return HttpResponse(message, mimetype='text/plain')

@csrf_exempt
def refresh_event_prices(request):
    if request.method == 'POST':
        event_id = request.POST['event_id']
        event = Event.objects.get(pk = event_id)
        prices = EventPrice.objects.filter(event = event)

        #return HttpResponse('woohaaa', mimetype='text/plain')
        context = Context({"prices":prices, })
        #return HttpResponse(context, mimetype='text/plain')
        return render_to_response('private/prices.html',context)

@csrf_exempt
def delete_event_price(request):
    if request.method == 'POST':
        price_id = request.POST['price_id']
        price = EventPrice.objects.get(pk = price_id)
        price.delete()
        return HttpResponse(price_id, mimetype="text/plain")
