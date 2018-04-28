from django.contrib import admin

# Register your models here.



from .models import (Profile, Ematt, Emsalary, Leave)

# Register your models here.

admin.site.register(Profile)

admin.site.register(Ematt)

admin.site.register(Emsalary)

admin.site.register(Leave)

