from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
import requests
from Account.models import Account
from django.http import HttpResponse
from django.utils.text import slugify
from hashlib import sha256
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from .forms import JobAlertForm
from django.utils import timezone
from django.db.models import Q
from django.contrib import messages
from Employee.models import Applylist,SavedJobs,Courses,Videos,Course_purchase,Feedback,sentiment
from Company.models import JobDetails,Selected,Applicants,JobAlert
from django.core.paginator import Paginator, EmptyPage,InvalidPage


# to view all job list
@login_required(login_url='login')
def joblist(request, template='Employee/joblist.html', extra_context=None):
    sorting = request.GET.get('sorting', 'recent')
    sorting_map = {
        'recent': '-date_posted',
        'oldest': 'date_posted',
        'expiry': 'enddate',
    }
    sorting_criterion = sorting_map.get(sorting, '-date_posted')

    jobtype_filters = request.GET.getlist('jobtype[]')

    applied_jobs = []
    if request.user.is_authenticated:
        applied_jobs = Applylist.objects.filter(cand=request.user).values_list('job_id', flat=True)

    if not jobtype_filters:
        user_category = request.user.category
        job_list = JobDetails.objects.filter(category=user_category, enddate__gte=timezone.now()).exclude(id__in=applied_jobs).order_by(sorting_criterion)
    else:
        job_list = JobDetails.objects.filter(jobtype__in=jobtype_filters, enddate__gte=timezone.now()).exclude(id__in=applied_jobs).order_by(sorting_criterion)

    paginator = Paginator(job_list, 5)
    page = request.GET.get('page')
    job_list = paginator.get_page(page)

    context = {
        'job_list': job_list,
        'selected_sorting': sorting,
        'jobtype_filters': jobtype_filters,
    }
    if extra_context is not None:
        context.update(extra_context)

    return render(request, template, context)



#to view profile
def profile(request):
    return render(request, 'Employee/Employee_profile.html')
 


        

#to view a individual job in  detail
@login_required(login_url='login')
def singlejob(request, id):
    Job=JobDetails.objects.filter(id=id)
    Job11=JobDetails.objects.get(id=id)
    already_applied = Applylist.objects.filter(job=Job11, cand=request.user).exists()
    saved_job = SavedJobs.objects.filter(user=request.user, job=Job11).exists()
    context={
        'Job':Job,
        'already_applied': already_applied,
        'saved_job': saved_job,
    }
    return render(request,'Employee/singlejob.html',context)  

# to update a profile
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
        district = request.POST.get('District')
        gender = request.POST.get('gender')
        profilepic = request.FILES.get('pic')
        category = request.POST.get('job-category')
        user_id = request.user.id
        
        user = Account.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        
        user.profilepic = profilepic
        user.gender = gender
        user.contact = contact
        user.address = address
        user.district = district
        user.country = country
        user.state = state
        
        # Check if category is already set
        if not user.category:
            user.category = category
            
        user.save()
        messages.success(request,'Profile Updated Successfully')
        return redirect('Eprofile')

   #userhome     
def userhome(request):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_authenticated:
        if request.user.is_employee:
          applied_jobs = Applylist.objects.filter(cand=request.user).values_list('job_id', flat=True)
          user_category = request.user.category
          Job=JobDetails.objects.filter(category=user_category, enddate__gte=timezone.now()).exclude(id__in=applied_jobs).order_by('-date_posted')[:3]
          c = Courses.objects.all()
          context={
           'job_list':Job,
           'c': c,
           'user': user,
          }
   return render(request,'Employee/userhome.html',context)


#searchbar code

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


@login_required(login_url='login')
def Apply(request,pk):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_employee:
        job=JobDetails.objects.get(id=pk)
       
    return render(request, 'Employee/Applyjob.html',{'user':user,'job':job}) 

def ApplyJob(request,id):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
      job=JobDetails.objects.get(id=id)
      notes=request.POST.get('notes')
      resume = request.FILES.get('resume')
      
      newapply=Applylist.objects.create(cand=user,job=job,notes=notes,resumes=resume)
      newapply.save()
      new=Applicants.objects.create(applicant=user,job=job,Resume=resume)
      new.save()

      return redirect("joblist")
    
   
@login_required(login_url='login')
def saved_jobs(request):
    job_list = SavedJobs.objects.filter(user=request.user).order_by('-date_posted')
    paginator = Paginator(job_list, 5) # Show 5 jobs per page
    page = request.GET.get('page')
    jobs = paginator.get_page(page)

    return render(request, 'Employee/saved_jobs.html', {'jobs': jobs})

@login_required(login_url='login')
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
        
    return redirect(request.META.get('HTTP_REFERER'))



@login_required(login_url='login')
def savedjob_delete(request, id):
    job = SavedJobs.objects.get(id=id)
  
    job.delete()

    return redirect("saved-jobs")


@login_required(login_url='login')
def search(request, template='Employee/joblist.html', extra_context=None):
    query = request.GET.get('query')
    sorting = request.GET.get('sorting', 'recent')
    sorting_map = {
        'recent': '-date_posted',
        'oldest': 'date_posted',
        'expiry': 'enddate',
    }
    sorting_criterion = sorting_map.get(sorting, '-date_posted')

    if query:
        job_list = JobDetails.objects.filter(
            Q(jobname__icontains=query) | Q(companyname__icontains=query)
        ).order_by(sorting_criterion)
    else:
        job_list = JobDetails.objects.all().order_by(sorting_criterion)

    paginator = Paginator(job_list, 5)
    page = request.GET.get('page')
    job_list = paginator.get_page(page)

    context = {
        'job_list': job_list,
        'selected_sorting': sorting,
    }
    if extra_context is not None:
        context.update(extra_context)

    return render(request, template, context)


@login_required(login_url='login')
def appliedjobs(request):
    user = Account.objects.get(email=request.session.get('email'))
    if request.user.is_employee:
        applied_jobs = Applylist.objects.filter(cand_id=user)
        paginator = Paginator(applied_jobs, 5)  # Show 10 items per page
        page = request.GET.get('page')
        applied_jobs = paginator.get_page(page)
        context = {'applied_jobs': applied_jobs}
        return render(request, 'Employee/applied_jobs.html', context)





def get_news(request):
    url = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=e92090481bc24996a2a89b1f90299cdf'
    response = requests.get(url)
    articles = response.json()['articles']

    # create a paginator with 10 items per page
    paginator = Paginator(articles, 10)
    
    # get the current page number from the request's GET parameters
    page_number = request.GET.get('page')
    
    # get the Page object for the current page number
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'Employee/news.html', {"page": "Newsplatform", "page_obj": page_obj})
  



def create_job_alert(request):
    if request.method == 'POST':
        form = JobAlertForm(request.POST)
        if form.is_valid():
            job_alert = form.save(commit=False)
            job_alert.user = request.user
            job_alert.save()
            # messages.success(request, 'Job alert created successfully.')
            return redirect('job_alerts')
    else:
        form = JobAlertForm()
    return render(request, 'Employee/myjobalert.html', {'form': form})


def job_alerts(request):
    job_alerts = JobAlert.objects.filter(user=request.user)

    for job_alert in job_alerts:
        matching_job_posts = JobDetails.objects.filter(
            jobname__icontains=job_alert.keywords,
            
            category__icontains=job_alert.industry,
            experience__icontains=job_alert.experience_level
        )

        if matching_job_posts.exists():
            send_job_alert_notification(request.user.email, matching_job_posts)

    return render(request, 'Employee/jobalert.html', {'job_alerts': job_alerts})


def send_job_alert_notification(email, matching_job_posts):
    subject = 'New Job Alert'
    message = render_to_string('Employee/job_alert_notification.html', {'matching_job_posts': matching_job_posts})
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])



@login_required(login_url='login')
def job_alerts_delete(request, id):
    job =JobAlert.objects.get(id=id)
  
    job.delete()

    return redirect("job_alerts")




def edit_job_alert(request, id):
    job_alert = get_object_or_404(JobAlert, id=id, user=request.user)

    if request.method == 'POST':
        form = JobAlertForm(request.POST, instance=job_alert)
        if form.is_valid():
            form.save()
            return redirect('job_alerts')
    else:
        form = JobAlertForm(instance=job_alert)

    return render(request, 'Employee/edit_job_alert.html', {'form': form})
