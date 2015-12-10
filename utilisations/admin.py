from django.contrib import admin
from .models import Allocation, Group, Person, Project

# Register your models here.
admin.site.register(Allocation)
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Project)