
from django.http import HttpResponse
from django.shortcuts import render
from libs.mysql import *







def home(req):

    print(list(Select("show tables;")))
    
    return render(req,'./index.html')


def addContent(req):
    print(req.form('name'))

    return render(req,'./pages/addcontent.html')


def addContentsubmit(res):
    print(req.form('name'))

