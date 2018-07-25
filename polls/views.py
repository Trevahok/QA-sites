from django.shortcuts import render
from .models import Faculty
from django.http import HttpResponse
from django.shortcuts import get_list_or_404,get_object_or_404
from .models import Faculty
from .forms import FacultyProfileForm
# Create your views here.
def test(request,department='scse'):
    instance =get_list_or_404(Faculty, dept = department)
    instance.sort(key=lambda i: i.post)
    print(instance[0].name)
    return render(request,'faculty.html',{'f' : instance,'len':len(instance)}) 
def fac_profile(request,department,pk):
    instance = get_object_or_404(Faculty,dept=department,id= pk)
    profile_update_form = FacultyProfileForm(request.POST or None,request.FILES or None,instance=instance)
    if profile_update_form.is_valid():
        profile_update_form.save()
    return render(request, 'faculty_profile.html', {'profile':profile_update_form})
