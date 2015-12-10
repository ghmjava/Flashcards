from django.http.response import HttpResponse
from .models import Group, Person 
from django.shortcuts import render_to_response
from utilisations.models import ROLE
# Create your views here.

def index(request):
    return HttpResponse("hello")

def all_groups(request):
    groups = Group.objects.all
    return render_to_response('utilisations/groups.html', {'groups': groups})

def group(request, group_id):
    group = Group.objects.filter(id = group_id).first()
    members = Person.objects.filter(group__id = group_id)
    manager = None
    deputy = None
    for member in members:
        if member.role == 'm':
            manager = member
        elif member.role == 'd':
            deputy = member
    return render_to_response('utilisations/group.html', {'group' : group, 'manager':manager, 'deputy':deputy, 'members':members})
