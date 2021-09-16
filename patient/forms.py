from django import forms

class Add_patient(forms.Form):

    patient_name=forms.CharField(max_length=20)
    contact_no=forms.IntegerField()
    addmission_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    ward_no = forms.IntegerField()
    amount= forms.IntegerField()
    disease=forms.CharField(max_length=40)


class Update_form(Add_patient):
   
    patient_name=forms.CharField(required=False)
    contact_no=forms.IntegerField(required=False)
    addmission_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}),required=False)
    ward_no = forms.IntegerField(required=False)
    amount= forms.IntegerField(required=False)
    disease=forms.CharField(required=False)

class Appointment_form(forms.Form):
    patient_name=forms.CharField(max_length=30)
    contact_no=forms.IntegerField()
    appointment_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    disease=forms.CharField(max_length=40)
