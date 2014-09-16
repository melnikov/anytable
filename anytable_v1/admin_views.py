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



def TheVenueAdministration(request, id):
         if  request.user.is_superuser:
            user = VenueAdministrator.objects.get( pk = id )
            venuetypes = VenueType.objects.filter(venue = user.venue)
            types = VenueType.objects.all()
            venuekitchens = VenueKitchen.objects.filter(venue = user.venue)
            kitchens = VenueKitchen.objects.all()
            venueoptions = VenueOptions.objects.filter(venue = user.venue)
            options = VenueOptions.objects.all()
            images = Venueimage.objects.filter(venue = user.venue)
            events = Event.objects.filter(venue = user.venue).order_by('-id')
            context = Context({"user":user, "venuetypes":venuetypes, "types":types, "venuekitchens":venuekitchens, "kitchens":kitchens, "venueoptions":venueoptions, "options":options, "images":images, "events":events})
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
def updatevenueemail(request):
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
def addevent(request):

    if request.method == 'POST':
        venuepk = request.POST['venuepk']
        the_venue = Venue.objects.get(pk = venuepk)
        the_date = datetime.datetime.strptime(str(datetime.date.today()), "%Y-%m-%d")
        file = request.FILES
        save_file(request.FILES['eventimg'])
        docfile = ('images/%s' % request.FILES['eventimg'])
        ev = Event.objects.create(title='title', image= docfile, date = the_date, venue = the_venue)
        ev.save()
        id= ev.id
        return HttpResponse(id, mimetype="text/plain")


@csrf_exempt
def deleteevent(request):
    if request.method == 'POST':
        eventid = request.POST['eventid']
        event = Event.objects.get(pk = eventid)
        event = event.delete()
        return HttpResponse('done', mimetype="text/plain")

@csrf_exempt
def updateevent(request):
    if request.method == 'POST':
        eventid = request.POST['eventid']
        eventtitle = request.POST['eventtitle']
        eventdescription = request.POST['eventdescription']
        ev = Event.objects.get(pk = eventid)
        ev.title = eventtitle
        ev.description = eventdescription
        ev.save()
        return HttpResponse('yep saved!', mimetype='text/plain')

@csrf_exempt
def updateeventimg(request):
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