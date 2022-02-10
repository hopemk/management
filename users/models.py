from django.db import models
from django.contrib.auth.models import User
from company.models import Company
# Create your models here.
class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = models.ImageField(default='default.png', upload_to = 'profile_pics')
    company = models.ForeignKey(Company,null=True, on_delete=models.CASCADE)
    #is_teacher = models.BooleanField(default=False)
    #dob = models.DateTimeField(auto_now_add=False,null = True, blank=True)
    gender = models.ForeignKey(Gender,null=True, on_delete=models.CASCADE)
    #first_name = models.CharField(max_length=25, blank=True, null=True)
    #last_name = models.CharField(max_length=25, blank=True, null=True)
    #reg_number = models.CharField(max_length=25, blank=True, null=True)
    nationality = models.CharField(max_length=25, blank=True, null=True)
    #faculty = models.ForeignKey(Faculty,null=True, on_delete=models.CASCADE)
    #department = models.ForeignKey(MyDepartment,null=True, on_delete=models.CASCADE)
    #id_number = models.CharField(max_length=25, blank=True, null=True)
    #id_number1 = models.CharField(max_length=25, blank=True, null=True)
