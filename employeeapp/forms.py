from django import forms
from .models import Employee

#normal form
class CompanyForm(forms.Form):
    company_name = forms.CharField(max_length=100)
    location = forms.CharField(max_length=100)
    total_emp = forms.IntegerField()

#model form
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'company_name', 'salary', 'date_of_joining', 'profile_pic']
        widgets = {
            'date_of_joining': forms.DateInput(attrs={'type': 'date'})
        }