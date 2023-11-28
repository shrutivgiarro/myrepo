from django.conf import settings
from django.urls import re_path as url

from UsersApp import views

urlpatterns=[
    
    url(r'^users$',views.userApi),
    url(r'^users/([0-9]+)$',views.userApi),
    url(r'^logs$',views.logsApi),
    url(r'^logs$/([0-9]+)$',views.logsApi),
    url(r'^pages$',views.pagesApi),
    url(r'^pages/([0-9]+)$',views.pagesApi),

    url(r'^login$',views.userLogin),
    
    url(r'^users/savefile',views.SaveFile)
]