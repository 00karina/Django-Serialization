from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
# Create your views here.

#Model object -single student Data

def detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    #print(serializer)
    #print('data',serializer.data)
    json_data=JSONRenderer().render(serializer.data)
    #print(json_data)
    return HttpResponse(json_data,content_type='application/json')


#Model object -single student Data

def details(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')