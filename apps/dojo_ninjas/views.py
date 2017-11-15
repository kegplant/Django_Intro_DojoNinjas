from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from models import *
# the index function is called when root is visited
def index(request):
    # Dojos.objects.all().delete()
    # Dojos.objects.create(name='CodingDojo Sillicon Valley',city='SJC',state='CA')
    # Dojos.objects.create(name='CodingDojo Seattle',city='Seattle',state='WA')
    # Dojos.objects.create(name='CodingDojo New York',city='NYC',state='NY')

    # Ninjas.objects.create(first_name='S',last_name='W',dojo=Dojos.objects.first())
    # Ninjas.objects.create(first_name='L',last_name='H',dojo=Dojos.objects.first())
    # Ninjas.objects.create(first_name='J',last_name='K',dojo=Dojos.objects.first())
    # Ninjas.objects.create(first_name='S2',last_name='W',dojo=Dojos.objects.get(state='NY'))
    # Ninjas.objects.create(first_name='L2',last_name='H',dojo=Dojos.objects.get(state='NY'))
    # Ninjas.objects.create(first_name='J2',last_name='K',dojo=Dojos.objects.get(state='NY'))
    # print Dojos.objects.get(state='WA').ninjas
    # print Ninjas.objects.filter(dojo=Dojos.objects.first())
    # for Gouse in Dojos.objects.all():
    #     print Gouse.objects.name
    context={
        'email': 'blog@gmail.com',
        'name': 'mike',
        'Dojos':Dojos,
        'Ninjas':Ninjas
    }

    #return HttpResponse(response)
    return render(request,'dojo_ninjas/index.html',context)