#This is where we'll add our patterns as we build the application. 

from django.urls import path
from django.conf.urls import url
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    #path('school/', views.SchoolsListView.as_view(), name='school'),
    path('school/', views.SchoolsList, name='school'),
    path('school/<int:pk>', views.SchoolDetail, name='school-detail'),
    #path('school/<int:pk>', views.SchoolsDetailView.as_view(), name='school-detail'),
    path('school/image', views.simple_upload, name='simple_upload' ),
    #url(r'^search/$', views.search, name='search'),
    #path(r'^search/$', views.SchoolsSearchListView.as_view(), name='search'),
    # url(r'\^school/(?P<pk>\\d+)/reviews/create/\$',
    # views.review,
    # name='review_create'),

]


