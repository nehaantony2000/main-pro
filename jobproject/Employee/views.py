from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from Account.models import Account
from django.http import HttpResponse
from django.utils.text import slugify
from hashlib import sha256


from django.db.models import Q
from django.contrib import messages
from django.contrib import messages, auth
from Employee.models import Applylist,SavedJobs,AppliedJobs,Courses,Videos,Course_purchase
from Company.models import JobDetails
from django.core.paginator import Paginator, EmptyPage,InvalidPage
def profile(request):
    return render(request, 'Employee/Employee_profile.html')
 
def cat(request):
    return render(request,'Employee/category.html')

        
@login_required(login_url='login')
def joblist(request):
    Job=JobDetails.objects.all().order_by('-date_posted')
    for i in Job:
      
     context={
        'job_list':Job
    }
    return render(request,'Employee/joblist.html',context)


@login_required(login_url='login')
def singlejob(request, id):
    Job=JobDetails.objects.filter(id=id)
    Job11=JobDetails.objects.get(id=id)

    context={
        'Job':Job,
       
    }
    return render(request,'Employee/singlejob.html',context)  
            
def Update_profile(request):
   if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('mobile')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        
        district=request.POST.get('District')
        gender = request.POST.get('gender')
        profilepic =request.FILES.get('pic')
        # skills=request.POST.get('skills')
        # languages=request.POST.get('languages')
        # education = request.POST.get('education')
        user_id = request.user.id
        
        user = Account.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        user.profilepic=profilepic
        user.gender=gender
        user.contact = contact
        user.address = address
        user.district=district
        user.country=country
        user.state=state
        user.save()
        messages.success(request,'Profile Are Successfully Updated. ')
        return redirect('Eprofile')

          


        
        
        

     
# def joblist(request):
#     J=Joblist.objects.all()
#     return render(request,'Employee/joblist.html',{'key1':J})



def userhome(request):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_authenticated:
        if request.user.is_employee:
          Job=JobDetails.objects.all()
          c = Courses.objects.all()
          context={
           'job_list':Job,
           'c': c,
           'user': user,
          }
   return render(request,'Employee/userhome.html',context)
def searchbar(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(jobname__icontains=query) | Q(companyname__icontains=query))
            J=JobDetails.objects.filter(multiple_q) 
            return render(request, 'searchbar.html', {'key1':J})
        else:
            messages.info(request, 'No search result!!!')
            print("No information to show")
    return render(request, 'searchbar.html', {}) 


@login_required
def Apply(request,pk):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_employee:
        job=JobDetails.objects.get(id=pk)
    return render(request, 'Employee/Applyjob.html',{'user':user,'job':job}) 

    
def ApplyJob(request,id):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
    job=JobDetails.objects.get(id=id)
    education=request.POST.get('edu')
    minsalary=request.POST.get('min')
    maxsalary=request.POST.get('max')
    resume=request.FILES.get('resume')
    
    newapply=Applylist.objects.create(cand=user,job=job,education=education,minsalary=minsalary,maxsalary=maxsalary,resume=resume)
    newapply.save()
   
    messages.success(request,'Applied Successfully ')
    return render(request,"Employee/Applyjob.html",{'user':user,'job':job})
   
@login_required
def saved_jobs(request):
    jobs = SavedJobs.objects.filter(user=request.user).order_by('-date_posted')
    return render(request, 'Employee/saved_jobs.html', {'jobs': jobs})

@login_required
def save_job(request,id):
   user = Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
      job = JobDetails.objects.get(id=id)
      print(job.id)
      saved_job, created = SavedJobs.objects.get_or_create(job_id=job.id, user=user)
     
   return redirect(request.META.get('HTTP_REFERER'))



@login_required
def saved_job_canceled(request,id):
    id = request.user.id
    job = SavedJobs.objects.get(id=id)
    job.delete()
    return redirect("Course/coursesenrolled")