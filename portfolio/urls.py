from django.urls import path
from .views import *

urlpatterns = [

    path('',homepage,name="home"),
    path('about/',aboutpage,name="about"),
    path('project/',projectpage,name="project"),
    path('exprience/',expriencepage,name="exprience"),
    path('certification/',certification,name="certification"),
    path('contect/',contectpage,name="contect"),
    path('resume/',resumepage,name="resume")
]