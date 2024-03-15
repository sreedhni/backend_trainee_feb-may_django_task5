from django.urls import path
from employeeapp import views

urlpatterns = [
    path("company/add/",views.add_company,name="company-add"),
    path("employee/add/",views.EmployeeCreateView.as_view(),name="employee-add"),
    path("company/all/",views.CompanyListView.as_view(),name="company-all"),
    path("employee/all/",views.EmployeeListView.as_view(),name="employee-all"),
    path('upload/', views.upload_file, name='upload_file'),
    path('files/', views.file_list, name='file_list'),

    path('', views.home, name='home')



]
