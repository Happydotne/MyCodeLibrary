from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseBadRequest
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
import logging
FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

import json

import simplejson


def add(request):
    try:
        if request.method == "POST":
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")

            qs = User.objects.filter(email=email)
            print(qs)
            print(type(qs))
            if qs:
                return HttpResponseBadRequest()

            user = User()
            user.email = email
            user.name = name
            user.password = password

            try:
                user.save()
                return HttpResponseRedirect('/index/')
            except Exception as e:
                raise
                return HttpResponse("添加成功")
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()

def edit(request):
    try:
        if request.method == "POST":
            id = request.POST.get("id")
            name = request.POST.get("name")
            email = request.POST.get("email")
            password = request.POST.get("password")
            print(id)
            print(name)
            print(email)
            # user = User()
            # user.email = email
            # user.name = name
            # user.password = password

            try:
                #user.save()
                User.objects.filter(id=id).update(name=name, email=email, password=password)
                return HttpResponseRedirect('/index/')
            except Exception as e:
                raise
                return HttpResponse("添加成功")
    except Exception as e:
        logging.info(e)
        return HttpResponseBadRequest()

def deleteData(request):
    try:
        if request.method == "POST":
            id = request.POST.get("id")
            # print("woowowow")
            # print(id)
            print("sssssssssssss")
            User.objects.filter(pk=id).delete()
    except Exception as e:
        raise
        return HttpResponse("添加成功")
    return HttpResponseRedirect('/index/')



def showAdd(request):
    #print("123456")
    return render(request,'add.html')

def showEdit(request):
    if request.method == "GET":
        id = request.GET.get("id")
        print("woowowow")
        print(id)
        data = User.objects.get(pk=id)
        print(data)
        return render(request, 'edit.html',{'data': data})

def getAll(request):
    # print(request)
    # print("123")
    data = User.objects.all()
    #print(data)
    return render(request,'index.html',{'data':data})