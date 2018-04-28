from django import forms

from .models import Profile, Ematt, Emsalary,Leave

class Profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user','name','employee_id','address','joindate','birth_date','phone_number','resigndate','work_all','image',)


class EmattForm(forms.ModelForm):
    class Meta:
        model = Ematt
        fields = ('date','shift','status','reason',)


class EmsalaryForm(forms.ModelForm):
    class Meta:
        model = Emsalary
        fields = ('user','year','month','amount','status',)


class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = ('reason','status',)

