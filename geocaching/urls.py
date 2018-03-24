"""geocaching URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from geoposts import views as geoposts_views



urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^logout/',geoposts_views.logout_view,name= 'logout'),
    url(r'^login/',geoposts_views.login_view,name ='login'),
    url(r'^home/',geoposts_views.home,name = 'main-home'),
    url(r'^project-portal/',geoposts_views.show_caching_projects,name = 'show-projects-portal'),
    url(r'^geoposts/',geoposts_views.show_project_posts,name ='show-posts'),
    url(r'^collectgeopost-info',geoposts_views.collect_geopostInfo,name = 'collect-geopost'),
    url(r'^list-of-students',geoposts_views.StudentList.as_view(),name = 'list-of-students'),
    path(r'students/<int:pk>',geoposts_views.StudentDetail.as_view(),name = 'list-of-students'),

]
