import json
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
from .ImageForm import GeoImageForm



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
    list_of_id=[]
    user = request.user
    project_title = request.GET.get('name')
    id = Geoproject.objects.get(name = project_title).id
    posts = Geopost.objects.filter(geoproject=id)
    user_query_set = GeopostStudent.objects.filter(user=request.user)

    for id in user_query_set:
        list_of_id.append(id.geo_post_id)
    refined_query_set = posts.exclude(id__in = list_of_id)

    return render( request,'list-of-posts.html',{'posts':refined_query_set})

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

    if request.method == 'POST' and request.FILES['imageupload']:
        image = request.FILES['imageupload']

    image_object = Image(image = image)

    c = image_object.save()
    student_geopost_image = Image.objects.get(id = c)

    student_geopost = GeopostStudent(name=name,
                                     latitude=latitude,
                                     longitude=longitude,
                                     description=description,
                                     city=city,
                                     result=result,
                                     user=request.user,
                                     done=True,
                                     geo_post_id=geo_post_update_object.id,
                                     image = student_geopost_image)


    queryset = GeopostStudent.objects.filter(done =True ,user = request.user)
    context = {'posts':queryset}



    student_geopost.save()
    return render(request,'students-specimen-list.html',context)




class StudentList(generic.ListView):


    model = Geoproject
    template_name = 'list-of-students.html'
    context_object_name = 'project_list'



class StudentDetail(generic.ListView):
    model = GeopostStudent
    template_name = 'list-of-students-detail.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        # original qs
        qs = super().get_queryset()
        # filter by a variable captured from url, for example
        return qs.filter(user = self.kwargs['pk'])


@staff_member_required(redirect_field_name='main-home')
def project_students_list(request):

    dict_students = {}
    if request.method == 'POST' and request.is_ajax():

        project_name = request.POST['name']
        print(project_name)


        student_object = Geoproject.objects.get(name = project_name ).user

        for user in student_object.all():
            total = 0

            total_object = GeopostStudent.objects.filter(user = user.id)


            for t in total_object:
                print(t.grade)
                try:

                    total = total + int(t.grade)
                except:
                    total = total + 0


            dict_students[user.username] = str(total)+(",")+str(user.id)


        print(dict_students)


    return HttpResponse(json.dumps({'students': dict_students}), content_type="application/json")


@staff_member_required(redirect_field_name='main-home')
def updateGrade(request):
    if request.method =='POST':
        pk = request.POST['grade_id']
        grade = request.POST['grade']

    goto_id = GeopostStudent.objects.get(id = pk).user.pk

    GeopostStudent.objects.filter(pk=pk).update(grade=grade)

    link = "/students/" + str(goto_id)
    return HttpResponseRedirect(link)


def show_personal_grade(request):

    print("hello personal grade")

    total = 0
    dict_students = {}
    if request.method == 'POST' and request.is_ajax():

        project_name = request.POST['name']

        student_object = Geoproject.objects.get(name=project_name).user

        for user in student_object.all():
            print(user.username,request.user)

            if (str(user.username) == str(request.user)):


                total_object = GeopostStudent.objects.filter(user=user.id)
                print(total_object)

                for t in total_object:
                    print(t.grade)
                    try:

                        total = total + int(t.grade)
                    except:
                        total = total + 0

                print(total)

                dict_students[user.username] = total

    print(dict_students)

    return HttpResponse(json.dumps({'students': dict_students}), content_type="application/json")

























