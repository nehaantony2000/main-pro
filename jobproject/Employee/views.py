from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from Account.models import Account
from django.http import HttpResponse
from django.utils.text import slugify
from hashlib import sha256

from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from Employee.models import Applylist,SavedJobs,Courses,Videos,Course_purchase
from Company.models import JobDetails
from django.core.paginator import Paginator, EmptyPage,InvalidPage

from django.core.paginator import Paginator
from django.shortcuts import render

def joblist(request, template='Employee/joblist.html', extra_context=None):
    # Get the selected sorting option from the request
    sorting = request.GET.get('sorting', 'recent')

    # Define a mapping between option values and sorting criteria
    sorting_map = {
        'recent': 'date_posted',
        'oldest': 'date_posted',
        'expiry': 'enddate',
      
    }

    # Get the corresponding sorting criterion from the mapping
    sorting_criterion = sorting_map.get(sorting, 'date_posted')

    # Retrieve the list of job details from the database and sort it
    job_list = JobDetails.objects.all().order_by(sorting_criterion)

    # Set the number of items to display per page and get the current page number
    paginator = Paginator(job_list, 1)
    page = request.GET.get('page')

    # Get the page object containing the list of job details to display
    job_list = paginator.get_page(page)

    context = {
        'job_list': job_list,
        'selected_sorting': sorting,
    }

    # Add any extra context provided to the function
    if extra_context is not None:
        context.update(extra_context)

    return render(request, template, context)


def profile(request):
    return render(request, 'Employee/Employee_profile.html')
 
def cat(request):
    return render(request,'Employee/category.html')

        


@login_required(login_url='login')
def singlejob(request, id):
    Job=JobDetails.objects.filter(id=id)
    Job11=JobDetails.objects.get(id=id)

    context={
        'Job':Job,
       
    }
    return render(request,'Employee/singlejob.html',context)  


@login_required(login_url='login')         
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
        messages.success(request,'Profile  Updated Successfully ')
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

@login_required(login_url='login')
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
    job_list = SavedJobs.objects.filter(user=request.user).order_by('-date_posted')
    paginator = Paginator(job_list, 1) # Show 5 jobs per page
    page = request.GET.get('page')
    jobs = paginator.get_page(page)

    return render(request, 'Employee/saved_jobs.html', {'jobs': jobs})

@login_required
def save_job(request,id):
    user = Account.objects.get(email=request.session.get('email'))
    if request.user.is_employee:
      job = JobDetails.objects.get(id=id)
      try:
         saved_job = SavedJobs.objects.get(job_id=job.id, user=user)
         if saved_job.is_saved:
            saved_job.is_saved = False
            saved_job.save()
         else:
            saved_job.is_saved = True
            saved_job.save()
      except SavedJobs.DoesNotExist:
         SavedJobs.objects.create(job_id=job.id, user=user, is_saved=True)
         messages.success(request,'Job Saved For Later ')
    return redirect(request.META.get('HTTP_REFERER'))



@login_required
def savedjob_delete(request, id):
    job = SavedJobs.objects.get(id=id)
    messages.warning(request,'Are you Sure U want to Delete ? ')
    job.delete()
    messages.success(request,'Deleted Successfully!! ')
    return redirect("saved-jobs")


@login_required(login_url='login')
def search(request):
    if request.method == 'GET':
        query = request.GET.get('query')
        if query:
            multiple_q = Q(Q(jobname__icontains=query) | Q(companyname__icontains=query))
            J=JobDetails.objects.filter(multiple_q) 
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            messages.info(request, 'No search result!!!')
            print("No information to show")
    return redirect(request.META.get('HTTP_REFERER'))


@login_required(login_url='login')
def appliedjobs(request):
    user = Account.objects.get(email=request.session.get('email'))
    if request.user.is_employee:
        applied_jobs = Applylist.objects.filter(cand_id=user)
        paginator = Paginator(applied_jobs, 10)  # Show 10 items per page
        page = request.GET.get('page')
        applied_jobs = paginator.get_page(page)
        context = {'applied_jobs': applied_jobs}
        return render(request, 'Employee/applied_jobs.html', context)

  