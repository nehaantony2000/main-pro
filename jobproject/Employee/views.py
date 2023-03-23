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



def userhome(request,c_slug=None,v_slug=None):
    Job=JobDetails.objects.all().order_by('-date_posted')
    std=Account.objects.get(email=request.session.get('email'))
    context={
        'job_list':Job
    }
    if request.user.is_authenticated:
       
        if request.user.is_employee:
            email = request.session.get('email')
            c_videos = None
            video_key=None
            if c_slug!=None:
              course=get_object_or_404(Courses,slug=c_slug)
              print(course.pk)
              videos=Videos.objects.filter(course_id=course.pk)
              paginator=Paginator(videos,2)     # 10 videos per page
              try:
                  page=int(request.GET.get('page','1'))
              except:
                  page=1
              try:
                 videos=paginator.page(page)
              except (EmptyPage,InvalidPage):
                  videos=paginator.page(paginator.num_pages)
              if v_slug and c_slug!=None:
                 video = get_object_or_404(Videos, slug=v_slug)
                 print(video.course_id)
                 context={
                     'job_list':Job,
                      "c_videos":videos,
                      "std":std
                   }
                 return render(request, 'Employee/userhome.html',{"c_videos":videos,"video_key": video,"std":std})

              return render(request, 'Employee/userhome.html')

            else:
                id=request.user.id
                courses=Courses.objects.all()
                std=Account.objects.get(email=request.session.get('email'))
                return render(request,'Employee/userhome.html',{'std':std,'courses':courses})


    
 
    return render(request, 'Employee/userhome.html',context)

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
    jobs = SavedJobs.objects.filter(
        user=request.user).order_by('-date_posted')
    return render(request, 'Employee/saved_jobs.html', {'jobs': jobs})


@login_required
def save_job(request):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
     job=JobDetails.objects.all()
     saved, created = SavedJobs.objects.create(job=job,user=user)
   return render(request, 'Employee/singlejob.html', {'job': job})

