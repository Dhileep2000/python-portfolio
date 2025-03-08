from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage
from .models import *
from .forms import *
from django.views.decorators.csrf import requires_csrf_token

def homepage(request):
    return render(request,'home.html')

def aboutpage(request):
    return render(request,'about.html')

def projectpage(request):

    context=[

        
        {
            'title':'weatherapp',
            'path':'images/weather.jpg.png',
        },

         {
            'title':'spotify',
            'path':'images/spotify.jpg',
        },

        {
            'title':'student management',
            'path':'images/student.jpg.png',

        },

        {
            'title':'ecommerce',
            'path':'images/ecommerce.jpg',

        },
        {
            'title':'portfolio',
            'path':'images/image.png',

        },
          {
            'title':'tailwind-blog',
            'path':'images/blog.png',

        },
    ]
    return render(request,'project.html',{"context":context})

def expriencepage(request):

    context=[
        {
            'company':'VR service',
            'position':' SEO Analyst',

        }
    ]


    return render(request,'exprience.html',{"context":context})

def certification(request):

    context=[
        {
            'certification':'digital marketing',
            'add':'add image',

        }
    ]

    return render(request,'certification.html',{"context":context})

def contectpage(request):

    if request.method == 'POST':
        print(request.POST)

        contact = model_port(name = request.POST['name'], email = request.POST['email'], phonenumber = request.POST['phonenumber'], message = request.POST['message'])

        contact.save()


    return render(request,'contect.html')



def resumepage(request):
   resume_path="myapp/COM CERT.pdf"
   resume_path=staticfiles_storage.path(resume_path)

   if staticfiles_storage.exists(resume_path):
       with open(resume_path,"rb") as resume_file:
           response=HttpResponse(resume_file.read(),content_type="application/pdf")
           response['content-disposition']='attachment';filename="COM CERT.pdf"
           return response
   else:
       return HttpResponse("resume not found",status=404)
   
   #you can download the pdf ,fst write the in properly,become run the comment in python manage.py collectstatic
    
