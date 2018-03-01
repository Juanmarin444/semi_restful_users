from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages
def index(request):

    return render(request, 'users/index.html', {'users': User.objects.all()})

def addnew(request):

    return render(request, 'users/addnew.html')

def create(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/user/new')
    else:
        User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])
        return redirect('/')

def show(request, user_id):
    my_user = User.objects.get(id=user_id)
    return render(request, 'users/show.html', {'user': my_user})

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')

def edit(request, user_id):
    my_user = User.objects.get(id=user_id)
    return render(request, 'users/edit.html', {'user': my_user})

def update(request, user_id):

    errors = User.objects.basic_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
            return redirect('/user/edit/' + user_id)
    else:
        b = User.objects.get(id=user_id)
        b.first_name = request.POST['first_name']
        b.last_name = request.POST['last_name']
        b.email = request.POST['email']
        b.save()
        return redirect('/user/show/' + user_id)