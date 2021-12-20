from django.shortcuts import render

from  materials.models import Material

# Create your views here.


def home_material_view(request):
    object_list = Material.objects.all()
    return render(request,'home_material.html',{'object_list':object_list,'nav':'home'})
