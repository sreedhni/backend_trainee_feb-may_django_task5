from django.db import models

class Company(models.Model):
    company_name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    total_emp=models.PositiveIntegerField()

    def __str__(self):
        return self.company_name
    
class Employee(models.Model):
    employee_name=models.CharField(max_length=70)
    company_name=models.ForeignKey(Company,on_delete=models.CASCADE)
    salary=models.PositiveIntegerField()
    date_of_joining=models.DateField()
    profile_pic=models.ImageField(upload_to="images",null=True)
    def __str__(self):
        return self.employee_name
    
class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploads/',null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)


