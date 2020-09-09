from django.shortcuts import render
from  News_app.models import employee

# Create your views here.
def home_view(request):
    return render(request,'News_app/home.html')

def emp_info_view(request):
     employees = employee.objects.all()
     return render(request,'News_app/empdata.html',{'employees':employees})
