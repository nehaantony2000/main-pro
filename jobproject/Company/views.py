from django.shortcuts import render,redirect
import sweetify
from django.contrib.auth.decorators import login_required
from Account.models import Account
from Employee.models import Applylist,Courses,Course_purchase,Videos
from Company.models import JobDetails,Applicants,Selected
from django.contrib import messages, auth
from django.utils.text import slugify
from hashlib import sha256
from Course.forms import VideoForm

def Companyhome(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_company:
         p=JobDetails.objects.filter(email_id=request.user)
         context = {
             'p': p,
             'user' : user ,
         }
    return render(request,'Comp/index.html',context)

@login_required
def postjob(request):
    user=Account.objects.get(email=request.session.get('email'))
    return render(request,'Comp/JobPost.html')

@login_required
def postedjob(request):
     user=Account.objects.get(email=request.session.get('email'))
     if request.user.is_authenticated:
        if request.user.is_company:
            p=JobDetails.objects.filter(email_id=request.user)
     return render(request, 'Comp/Postedjoblist.html',{'p':p})

@login_required
def profile(request):
    user=Account.objects.get(email=request.session.get('email'))
    return render(request, 'Comp/Company_profile.html')
 
@login_required
def JobdetailSubmit(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_company:
       jobname=request.POST['jobname']
       companyname=request.POST['Cname']
       companyaddress=request.POST['add']
       jobdescription=request.POST['Description']
       qualification=request.POST['qualification']
       responsibility=request.POST['Response']
       location=request.POST['location']
       experience=request.POST['exp']
       salarypackage=request.POST['salary']
       companywebsite=request.POST['web']
       logo=request.FILES['logo']
       companycontact=request.POST['mobile']
       enddate=request.POST['enddate']
       tagline=request.POST['tagline']
       category=request.POST['category']
       newjob=JobDetails.objects.create(jobname=jobname,companyname=companyname,companyaddress=companyaddress,qualification=qualification,jobdescription=jobdescription,responsibility=responsibility,location=location,experience=experience,companycontact=companycontact,companywebsite=companywebsite,salarypackage=salarypackage,logo=logo,enddate=enddate,category=category,tagline=tagline)
       messages.success(request,'Job Posted ')
       return render(request,"Comp/jobPost.html")
        
@login_required
def Update_profile(request):
   if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        contact = request.POST.get('mobile')
        address = request.POST.get('address')
        country = request.POST.get('country')
        state = request.POST.get('state')
        dob = request.POST.get('dob')
        district=request.POST.get('District')
        gender = request.POST.get('gender')
        profilepic =request.FILES['pic']
        jobtype=request.POST.get('jobtype')
        # skills=request.POST.get('skills')
        # languages=request.POST.get('languages')
        # education = request.POST.get('education')
        user_id = request.user.id
        
        user = Account.objects.get(id=user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.contact = contact
        user.address = address
        user.district=district
        user.country=country
        user.state=state
        user.jobtype=jobtype
        user.profilepic =profilepic 
        user.save()
        sweetify.success(request,'Profile Are Successfully Updated. ')
        return redirect('profile')
   
@login_required
def JobApplylist(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_company:
            Apply=Applicants.objects.filter()
    return render(request,"Comp/Applylist.html",{'Apply':Apply}) 


@login_required
def enrolledcandidate(request):
        user_id = request.user.id
        user = Account.objects.get(id=user_id)
        print(user)
        if request.user.is_company:
         print(request.user.id)
         c = Courses.objects.get(userid_id=user)
         print(request.user.id)
        purchase_stds=Course_purchase.objects.filter(course_id=c.id).values_list('userid',flat=True)
        std=Account.objects.filter(id__in=purchase_stds)
        print(list(std))
        return render(request, 'Courses/EnrolledCandidates.html',{'course':c,'std':std})

# def instructorviewfeedback(request):
#         ins = Account.objects.filter(user_id=request.user.id)
#         course=Courses.objects.get(user_id=request.user.id)
#         feed = Feedback.objects.filter(course_id=course.id)
#         std_ids=feed.values_list("user_id",flat=True)
#         std=RegisteredStudent.objects.filter(user_id__in=std_ids)
#         std_feed=zip(feed,std)
#         return render(request, 'instructorviewfeedback.html', {'ins': ins, 'std_feed': std_feed})

@login_required
def AddVideo(request):
    form=VideoForm()
    if request.method=='POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            course=form.cleaned_data['course']
            video=form.cleaned_data['video']
            Videos.objects.create(title=title,slug=slugify(title),course=course,video=video).save()
            return redirect("Companyhome")
    return render(request,"Courses/Add_Video.html",{"form":form})

@login_required
def jobdelete(request, id):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_company:
            job = JobDetails.objects.get(id=id)
            job.delete()
    return redirect("postedjob")


@login_required
def deleteApplication(request, id):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_company:
           job = Applylist.objects.get(id=id)
           job.delete()
    return redirect("Applylist")