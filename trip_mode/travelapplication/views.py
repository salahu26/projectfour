from pickle import GET

from django.shortcuts import render
from django.http import HttpResponse
from . models import picture
from . models import my_team


def trail(reque):
    #    character="the value is replaced"
    obj=picture.objects.all()
    obj2=my_team.objects.all()
    return render(reque,'index.html',{'value':obj,'result':obj2})







#    return render(reque, 'app_file.html', {'asd': character})
#def about(asd):
#    return render(asd,'about.html')
#def content(detl):
#    return HttpResponse('i dont know, how i live this world')
#def addition(values):
#    x=int(values.GET['first'])
#    y=int(values.GET['second'])
#    z=x+y
#    return render(values,'result.html',{'rec':z})

#def fun_static(rec):
 #   return render(rec,'index.tml')