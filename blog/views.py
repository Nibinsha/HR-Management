from django.shortcuts import render

from .models import Profile, Ematt, Emsalary, Leave
from .forms import Profileform,EmattForm, EmsalaryForm, LeaveForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.utils import timezone
from .forms import Profileform, EmattForm, EmsalaryForm
from django.contrib.auth.decorators import login_required

	
# Create your views here.
# starting page
def index(request):
    return render(request, 'start.html', {})


# USER DETAILS FOR USER
#user deatil for a user. here no edit option  but attendance can add
@login_required
def user_detail(request):  
    if request.user.is_authenticated():
       try:
          post = Profile.objects.get(user=request.user, user__is_active = True)
       except:
          post = {}
       try:
          att = Ematt.objects.filter(user=request.user, user__is_active = True) 
       except:
          att = {}
       try:
           sal = Emsalary.objects.get(user=request.user, user__is_active = True)
       except:
           sal = {}
       try:
           lve = Leave.objects.filter(user=request.user, user__is_active = True)
       except:
           lve = {} 
       
    return render(request, 'user_detail.html', {'post': post,'sal':sal,'att':att,'lve':lve})


# shwowing the emloyees name down by down FOR ADMIN
@user_passes_test(lambda u: u.is_superuser)
def administration(request):
    posts = Profile.objects.all()
    return render(request, 'admin.html', {'posts': posts})




# SHOWING USER DEATIL IN ADMIN SIDE
# user detail in admin side. here the edit option is available
@user_passes_test(lambda u: u.is_superuser)
def post_detail(request, pk):
    if request.user.is_authenticated():
       
       try:
           post = Profile.objects.get( pk=pk)
       except:
           post = {}
       
       usr = User.objects.get(pk = pk)
       print usr
      
       
       try:
           att = Ematt.objects.filter(user=usr) 
       except:
           att = Ematt.objects.create(user=usr)
       try:
           sal = Emsalary.objects.get(pk=pk)
       except:
           sal = {}
       try:
           lve = Leave.objects.filter(user=usr) 	
       except:
           lve = {}
 
      
    return render(request, 'ADMIN_user_detail.html', {'post': post,'sal':sal,'att':att,'lve':lve})


# Attendace editing passing ADMIN
@user_passes_test(lambda u: u.is_superuser)
def att_details(request, pk):
    if request.user.is_authenticated():       
      # usr = User.objects.get(pk = pk)    
       try:
           att = Ematt.objects.filter(id=pk) 
      
       except:
           att = Ematt.objects.create(id=pk) 
            
      
 
      
    return render(request, 'att_details_admin.html', {'att':att})


# LEAVE editing passing ADMIN
@user_passes_test(lambda u: u.is_superuser)
def leave_details(request, pk):
    
    if request.user.is_authenticated():   
    
       try:
           lve = Leave.objects.filter(id=pk) 	
       except:
           lve = Leave.objects.create(id=pk) 
    return render(request, 'leave_details_admin.html', {'lve':lve})








# ADD ATTENDANCE FOR USER. 
# add a attendance for user. edit option for user 
@login_required
def add_attendance(request):
    post = None
    if request.method == "POST":
        form = EmattForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
	    post.user = request.user
            post.save()
            return redirect('user_detail')
    else:
        form = EmattForm()
    return render(request, 'post_new.html', {'form': form})

# EDIT ATTENDANCE FOR ADMIN
#attendance editing for admin
@login_required
def att_edit(request, pk):
    post = Ematt.objects.get( pk=pk)
    if request.method == "POST":
        form = EmattForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.published_date = timezone.now()
            post.save()
            return redirect('att_details', pk=post.pk)
    else:
        form = EmattForm(instance=post)
    return render(request, 'post_new.html', {'form': form})





# ADDING PROFILE
# profile adding datas for admin 
@user_passes_test(lambda u: u.is_superuser)
def profile(request):
    post = None
    if request.method == "POST":
        form = Profileform(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Profileform()
    return render(request, 'profile.html', {'form': form})

#EDITING PROFILE
#profile editing for admin 
@login_required
def profile_edit(request, pk):
    post = Profile.objects.get( pk=pk)
    print post
    if request.method == "POST":
        form = Profileform(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Profileform(instance=post)
    return render(request, 'profile.html', {'form': form})

  





# EDITING SALARY
# salary edit option for admin in user account
def salary_edit(request, pk):
    post = Emsalary.objects.get( pk=pk)
    if request.method == "POST":
        form = EmsalaryForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = EmsalaryForm(instance=post)
    return render(request, 'post_new.html', {'form': form})

# ADDING SALARY
# salary adding datas for admin 
@user_passes_test(lambda u: u.is_superuser)
def salary(request):
    post = None
    if request.method == "POST":
        form = EmsalaryForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = EmsalaryForm()
    return render(request, 'salary.html', {'form': form})



# ADD LEAVE USER
#FOr USER
@login_required
def Leaveapp(request):
    post = None
    if request.method == "POST":
        form = LeaveForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('user_detail')
    else:
        form = LeaveForm()
    return render(request, 'leaveapp.html', {'form': form})


# EDIT LEAVE FOR ADMIN
#LEAVE editing for admin
@login_required
def leave_edit(request, pk):
    
    post = Leave.objects.get( pk=pk)
    if request.method == "POST":
        form = LeaveForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.published_date = timezone.now()
            post.save()
            return redirect('leave_details', pk=post.pk)
    else:
        form = LeaveForm(instance=post)
    return render(request, 'post_new.html', {'form': form})

   









      



