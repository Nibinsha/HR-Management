from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    employee_id = models.IntegerField()
    name = models.CharField(max_length=8,null=True, blank=True )
    address = models.TextField(max_length=500, blank=True)
    joindate = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,11}$', message="Phone number in the format: '+999999999'. Up to 11 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True) # validators should be a list
    resigndate = models.DateField(null=True, blank=True)
    work_all = models.CharField(max_length=8,null=True, blank=True )
    image = models.FileField(upload_to='media/',null = True, blank=True)
    
    

    def __str__(self):
        return str(self.user)


class Ematt(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    date = models.DateField(null=True, blank=True)
    SHIFT_CHOICES = (('Night', 'Night'),('Day', 'Day'),)
    shift = models.CharField(max_length=6,choices=SHIFT_CHOICES, default='Day',)
    STATUS_CHOICES = (('Present', 'Present'),('Absent', 'Absent'),)
    status = models.CharField(max_length=8,choices=STATUS_CHOICES, default='Absent',)
    reason = models.TextField(max_length=150, blank=True)
   
    def __str__(self):
        return str(self.user)


class Emsalary(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    year = models.DateField(null=True, blank=True)
    month = models.DateField(null=True, blank=True)
    amount = models.IntegerField(default=0)
    STATUS_CHOICES = (('Approved', 'Approved'),('Denied', 'Denied'),('', ''))
    status = models.CharField(max_length=8,choices=STATUS_CHOICES, default='',)

    def __str__(self):
        return str(self.user)

class Leave(models.Model):
      user = models.ForeignKey(User, on_delete=models.CASCADE)  
      reason = models.TextField(max_length=150, blank=True)
      LEAVE_CHOICES = (('Approved', 'Approved'),('Denied', 'Denied'),('', ''))
      status = models.CharField(max_length=8,choices=LEAVE_CHOICES, default='',null=True, blank=True)

      def __str__(self):
        return str(self.user)
      

    




