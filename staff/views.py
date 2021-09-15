from django.shortcuts import render
from django.views import View
from patient.models import Add_detail


class Home(View):
    def get(self,request):
        content={
            'page_tittle': 'Home',
            'patient_detail':Add_detail.objects.all()
        }
        
        return render(request,'index.html',content)