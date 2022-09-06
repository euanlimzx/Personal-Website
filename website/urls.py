from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name='index'),
    path('mystories',views.mystories,name='mystories'),
    path('professional',views.professional,name='professional'),
    path('about',views.about,name='about')
]