#Django star rating is setteled in setting.py .. just to remember


from django.shortcuts import render
from django.views import generic

# something for pilow images !!
from django.conf import settings
import os.path
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect

from django.db.models import Q
from django.contrib import messages
# for image upload:
#from django.shortcuts import render
#from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.

from .models import Schools, Area, Kind, Review

def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_schools = Schools.objects.all().count()
    #num_instances=BookInstance.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    #num_authors=Author.objects.count()  # The 'all()' is implied by default.
        # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    # Render the HTML template index.html with the data in the context variable

    return render(
    request,
    'index.html',
    context={'num_schools':num_schools,'num_visits':num_visits},   
    )


# class SchoolsListView(generic.ListView):
#     model = Schools
#     paginate_by = 3


def SchoolsList(request):
    school_list_giza = Schools.objects.all().filter(area__name="Giza")
    school_list_cairo = Schools.objects.all().filter(area__name="Cairo")
    school_list_alex = Schools.objects.all().filter(area__name="Alexandria")
    
    return render(
        request,
        'Schools_list.html',
        context={'school_list_giza':school_list_giza, 'school_list_cairo':school_list_cairo,
         'school_list_alex':school_list_alex},
    )
    paginate_by = 3




# class SchoolsDetailView(generic.DetailView):
#     model = Schools


def SchoolDetail(request, pk):
    name = Schools.objects.get(pk=pk)
    
    return render(
        request,
        'School_detail.html',
        context={"name":name,},

    )
   
    


""" # something for pilow images !!
# keep it inmind .. i may need it later:

from django.conf import settings
import os.path
from datetime import datetime
from PIL import Image, ImageFont, ImageDraw
from django.http import HttpResponse
 
 
 
def custom_image(request):
    # The text we want to draw on the image, in this case the local time, e.g. "20:55:11":
    text = datetime.now().strftime('%H:%M:%S')
     
    # Specifying our background image (in this case a 200 x 75 pixels PNG image):
    base_image = os.path.join(settings.BASE_DIR, 'static/app_name/images/mido.jpg')
     
    # Specifying the font file:
    font_file = os.path.join(settings.BASE_DIR, 'static/app_name/fonts/Xacto Blade.ttf')
     
    # Font color (black specified as RGB) and size:
    font_color = (0, 0, 0)
    font_size = 36
     
    image = Image.open(base_image)
    font = ImageFont.truetype(font_file, font_size)
    draw = ImageDraw.Draw(image)
     
    # Drawing the text 34 pixels from the left edge and 18 pixels from the top:
    draw.text((34, 18), text, font=font, fill=font_color)
     
    # Saving the image to the Django response object:
    response = HttpResponse(content_type='image/png')
    image.save(response, 'PNG')
     
    return response
 """

# for image upload:

def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'simple_upload.html')


def search(request):
    if request.method== 'POST':
        srch = request.POST['srh']

        if srch:
            match = Schools.objects.filter(Q(name__icontains=srch)| Q(address__icontains=srch))

            if match:
                return render(request, 'search.html', {'sr':match})
            else:
                messages.error(request, 'No results found, try searching using another letters...')

        else:
            return HttpResponseRedirect('/search/')
    return render(request, 'search.html')  












# def review(request, pk):
#     school = get_object_or_404(Schools, pk=pk)
#     review = SchoolReview(
#           rating=request.POST['rating'],
#           comment=request.POST['comment'],
#           user=request.user,
#           school=school)
#     review.save()
#     return HttpResponseRedirect(reverse('name:school-detail', args=(name.id,)))