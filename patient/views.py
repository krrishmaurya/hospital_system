from patient import models
from django.shortcuts import redirect, render
from . import  forms
from django.views import View
from . import models
import patient

class Add_patient(View):
    def get(self,request):
        content={
            'page_tittle':'add_details',
            'patient_form':forms.Add_patient(),
           
        
        }
        return render(request,'new_patient.html',content)
    
    
    def post(self,request):
        patient_name=request.POST['patient_name']
        contact_no=request.POST['contact_no']
        addmission_date=request.POST['addmission_date']
        ward_no=request.POST['ward_no']
        amount=request.POST['amount']
        added_detail=models.Add_detail(
            patient_name=patient_name,
            contact_no=contact_no,
            addmission_date=addmission_date,
            ward_no=ward_no,
            amount=amount
        )
        added_detail.save()
        return redirect('/')



class Details(View):
    def get(self,request):
        patient_id=request.GET['patient_id']
        content={
            'page_tittle':'your  detail',
            'detail':models.Add_detail.objects.get(id = patient_id)
            }
        return render(request,'details.html',content)

class Update_detail(View):

    def get(self,request):
        patient_id=request.GET['patient_id']
        content={
            'page_tittle':'updated detail',
            'current_details':models.Add_detail.objects.get(id = patient_id),
             'update_form':forms.Update_form()
        }
        return render(request,'update.html',content)

    def post(self,request):
        patient_id=request.POST['patient_id']
        disease=request.POST['disease']
        ward_no=request.POST['ward_no']
        amount=request.POST['amount']
        got_discharge=request.POST.get('discharge',False)
        new_details=models.Add_detail.objects.get(id=patient_id)
        new_details.disease=new_details.disease if disease =='' else disease
        new_details.ward_no=new_details.ward_no if ward_no =='' else ward_no
        new_details.amount=new_details.amount if amount =='' else new_details.amount+eval(amount)
        new_details.got_discharge=got_discharge
        new_details.save()
        return redirect('/')




            