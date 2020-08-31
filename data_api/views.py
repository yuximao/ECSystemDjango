from json import dumps

from django.http import HttpResponse
from django.shortcuts import render
from data_api.dataModel.ECModel import ecModel, get_label


# Create your views here.

def get_json(request):
    if request.method=='POST':
        text=request.FILES.get('file')
        res=ecModel(text)
        number=str(res[0])
        result=get_label(number)
        print(result)
        return HttpResponse(dumps(result), content_type="application/json")
    else:
        return HttpResponse(dumps('Wrong Request'), content_type="application/json")