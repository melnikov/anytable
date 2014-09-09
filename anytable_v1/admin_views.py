# coding=utf-8
from django.shortcuts import *
from django.template import *
from django.views.decorators.csrf import csrf_exempt
from django.http import *
from .forms.private_forms import *
from anytable_v1.models import *
from anytable.settings import *
from imagekit.admin import AdminThumbnail



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
            context = Context({"user":user, "venuetypes":venuetypes, "types":types, "venuekitchens":venuekitchens, "kitchens":kitchens, "venueoptions":venueoptions, "options":options, "images":images})
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
                r = Document(title= 'request is post and %s' % venuepk, docfile = docfile)
                r.save()


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




