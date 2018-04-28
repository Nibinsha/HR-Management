"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include,url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from blog.views import index, user_detail, administration, post_detail, add_attendance,profile_edit, att_edit, salary_edit,profile, salary, Leaveapp, att_details, leave_edit,leave_details

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    ########## Project ############
    url(r'^$', index, name='index'),

 
    url(r'^user_detail/', user_detail, name='user_detail'),
    url(r'^administration/', administration, name='administration'),
    url(r'^accounts/', include('registration.backends.simple.urls')),

    url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),

    # edit posts
    url(r'^post/(?P<pk>\d+)/edit/$', profile_edit, name='profile_edit'),

    url(r'^attendance/(?P<pk>\d+)/edits/$', att_edit, name='att_edit'),

    url(r'^salary/(?P<pk>\d+)/edits/$', salary_edit, name='salary_edit'),
   
    url(r'^leave/(?P<pk>\d+)/edits/$', leave_edit, name='leave_edit'),
    
    # attendance page
    

    #for leave applying
    url(r'^Leaveapp/', Leaveapp, name='Leaveapp'),

    # for att edting passing
    url(r'^leave_details/(?P<pk>\d+)/$', leave_details, name='leave_details'),


    url(r'^att_details/(?P<pk>\d+)/$', att_details, name='att_details'),

    
   
 
    
    
     
    # add attendance for user
    url(r'^add_attendance/', add_attendance, name='add_attendance'),

    # add new information about user from admin
    url(r'^profile/', profile, name='profile'),
    url(r'^salary/', salary, name='salary'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)






