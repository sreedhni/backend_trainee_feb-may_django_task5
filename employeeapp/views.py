# views.py
from django.shortcuts import render, redirect
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy

from employeeapp.forms import CompanyForm,EmployeeForm  
from employeeapp.models import Company,Employee 

#home page
def home(request):
    return render(request, 'home.html')
# 3.Create a view for adding details to first model (Use normal forms)
def add_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            company = Company(
                company_name=form.cleaned_data['company_name'],
                location=form.cleaned_data['location'],
                total_emp=form.cleaned_data['total_emp']
            )
            company.save()
            return redirect('company-all')  
    else:
        form = CompanyForm()
    return render(request, 'company_create.html', {'form': form})
#4.Create a view for adding details to second model (Use model forms)
class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'employee_add.html'  
    success_url = reverse_lazy("employee-all")
# 5.Create views for listing created records of each model in a table
class CompanyListView(ListView):
    model = Company
    template_name = 'company_list.html'  
    context_object_name = 'companies'

class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'  
    context_object_name = 'employees'