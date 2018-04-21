from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *

def index(request):
    context = {
        'courses' : Course.objects.all(),
        'descriptions' : Description.objects.all()
    }
    return render(request, 'odin/index.html', context)

def create(request):
    errors = Course.objects.course_manager(request.POST)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/')

    errors1 = Description.objects.description_manager(request.POST)
    if len(errors1):
        for x, y in errors1.items():
            messages.error(request, y)
            return redirect('/')

    else:
        if request.method == 'POST':
            newcourse = Course.objects.create(
                name = request.POST['name']
            )
            courseinfo = Description.objects.create(
                desc = request.POST['description'],
                describing = newcourse
            )
            return redirect('/')
def confirm(request, userid):
    print (userid)
    context = {
        'courseinfo' : Course.objects.get(id=userid)
    }
    request.session['usersid'] = userid

    return render(request, 'odin/confirm.html', context)

def destroy(request, userid):
    print (userid)
    Course.objects.get(id=userid).delete()
    return redirect('/') 



# Create your views here.
