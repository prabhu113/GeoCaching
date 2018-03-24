from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User as auth_user
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Case, Count, When
from django.conf import settings
from django.contrib.auth import login,authenticate,logout
from django.contrib.admin.views.decorators import staff_member_required
from django.views import generic
from .forms import LoginForm
from .models import *
from django.contrib.auth.models import User



def home(request):
    context ={}
    return render(request,"home.html",context)

def logout_view(request):
    logout(request)
    context ={}
    return render(request,"home.html",context)

def login_view(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        print("In here")
        user = authenticate(username = username, password = password)
        login(request,user)
        return HttpResponseRedirect("/project-portal/")
    else:
        if not(request.user.is_authenticated):
            context ={'loginform':form}
            return render(request,"home.html",context)
        else:
            return HttpResponseRedirect("/home")



@login_required(redirect_field_name='main-home')
def show_caching_projects(request):
    user = request.user
    projects = Geoproject.objects.filter(user = user)
    return render(request,'list-of-projects.html',{'projects':projects})


@login_required(redirect_field_name='main-home')
def show_project_posts(request):
    user = request.user
    project_title = request.GET.get('name')
    id = Geoproject.objects.get(name = project_title).id
    posts = Geopost.objects.filter(geoproject=id)
    return render( request,'list-of-posts.html',{'posts':posts})

def collect_geopostInfo(request):
    list_of_experiments_inputs_dict={}
    for i in  request.POST:
        if "experimentinput_" in i:
            key = i.split("_")[1]
            list_of_experiments_inputs_dict[key] = (request.POST[i])

    geo_post_update_object = Geopost.objects.get(id = int(request.POST.get('primarykey')))
    name = geo_post_update_object.name
    latitude = geo_post_update_object.latitude
    longitude = geo_post_update_object.longitude
    description = geo_post_update_object.description
    city = geo_post_update_object.city
    result = list_of_experiments_inputs_dict

    student_geopost = GeopostStudent(name = name,
                                     latitude = latitude,
                                     longitude =  longitude,
                                     description = description,
                                     city = city,
                                     result = result,
                                     user = request.user,
                                     done = True)

    print(student_geopost.name,student_geopost.latitude,student_geopost.description,student_geopost.result)

    student_geopost.save()
    return HttpResponse("<h1> Successfully updated the experiment </h1>")


class StudentList(generic.ListView):
    model = User
    template_name = 'list-of-students.html'
    context_object_name = 'student_list'



class StudentDetail(generic.ListView):
    model = GeopostStudent
    template_name = 'list-of-students-detail.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        print (self.kwargs['pk'])
        return qs.filter(user = self.kwargs['pk'])
























