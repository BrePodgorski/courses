from django.shortcuts import render, redirect
from .models import Course

def index(request):
    context={
    'courses':Course.objects.all()
    }
    return render(request,'wireframe/index.html',context)

def show(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def confirm(request,id=None):
    context={
    'courses':Course.objects.filter(id=id)
    # 'name':Course.objects.filter(name=name),
    # 'description': Course.objects.filter(description=description)
    }
    return render(request, 'wireframe/delete.html',context)

def clear(request, id):
    Course.objects.get(id=id).delete()
    return redirect('/')
    # Course.objects.create(name=request.POST['name'], description=request.POST['description'])

        # remove=Course.objects.filter(id=id).delete()
