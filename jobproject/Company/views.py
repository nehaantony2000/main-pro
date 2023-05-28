from django.conf import settings
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
import sweetify
import spacy
from django.contrib.auth.decorators import login_required
from Account.models import Account
from Employee.models import Applylist,Courses,Course_purchase,Videos,Feedback
from Company.models import JobDetails,Selected,Applicants,JobAlert
from django.contrib import messages, auth
from django.utils.text import slugify
from hashlib import sha256
from Course.forms import VideoForm
from django.core.paginator import Paginator, EmptyPage,InvalidPage
from django.core.mail import send_mail
import PyPDF2
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from spacy.matcher import PhraseMatcher
from skillNer.general_params import SKILL_DB
from skillNer.skill_extractor_class import SkillExtractor
import numpy as np



def Companyhome(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_company:
         p=JobDetails.objects.filter(email_id=request.user).order_by('-date_posted')
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
    user = Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated and request.user.is_company:
        p = JobDetails.objects.filter(email_id=request.user)
        paginator = Paginator(p, 5) # Show 10 jobs per page
        page = request.GET.get('page')
        jobs = paginator.get_page(page)
        context={
         'jobs': jobs,
         'p':p,
        }
        return render(request, 'Comp/Postedjoblist.html',context)
    else:
        return HttpResponseForbidden()


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
        
def edit_jobdetails(request,id):
    job = JobDetails.objects.get(id=id)
    if request.method == 'POST':
        job.jobname = request.POST['jobname']
        job.companyname = request.POST['companyname']
        job.jobtype = request.POST['jobtype']
        job.category = request.POST['category']
        job.qualification = request.POST['qualification']
        job.jobdescription = request.POST['jobdescription']
        job.responsibility = request.POST['responsibility']
        job.experience = request.POST['experience']
        job.location = request.POST['location']
        job.salarypackage = request.POST['salarypackage']
        job.companywebsite = request.POST['companywebsite']
        job.logo = request.FILES.get('logo') or job.logo
        job.companycontact = request.POST['companycontact']
        job.enddate = request.POST['enddate']
        job.tagline = request.POST['tagline']
        job.skills = request.POST['skills']
        job.save()
        return redirect('postedjob',id=job.id)

    context = {'job': job}
    return render(request, 'Comp/edit_jobdetails.html', context)








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
    user = Account.objects.get(email=request.session.get('email'))
    nlp = spacy.load("en_core_web_sm")
    skill_extractor = SkillExtractor(nlp, SKILL_DB, PhraseMatcher)
    ranked_applicants = []
    seen_candidate_ids = set()
    unique_ranked_applicants=[]
    if user.is_authenticated and user.is_company:
        jobs = JobDetails.objects.filter(email=user)
       
        jobname_filter = request.GET.get('jobname')
        jobdetails = None
        jobrequiredskills = []

        if jobname_filter is not None:
            try:
                jobdetails = JobDetails.objects.get(jobname=jobname_filter)
                jobrequiredskills = jobdetails.skills
            except JobDetails.DoesNotExist:
                pass
       
        if jobname_filter:
            applicants={}
            annotation2 = skill_extractor.annotate(jobrequiredskills)
            expectedskills =annotation2['results']
            expectedskills.keys()
            fullmatch1 = expectedskills['full_matches']
            ngrams_scored1 = expectedskills['ngram_scored']
            a_key1 = "doc_node_value"

            f_docnodevalues1 = [a_dict1[a_key1] for a_dict1 in fullmatch1]
            n_docnodevalues1 = [a_dict1[a_key1] for a_dict1 in ngrams_scored1]
        
            requiredskills = f_docnodevalues1 + n_docnodevalues1
            # print(requiredskills)
            sanitized_values = list(set(requiredskills)) 
            #print(sanitized_values)


            applications = Applylist.objects.filter(job__in=jobs, job__jobname=jobname_filter).order_by('applieddate')
            for application in applications:
                candidate_id=application.cand_id
                resume_path=application.resumes.path
                application_id = application.id

                with open(resume_path,'rb') as filehandle:
                    pdfReader = PyPDF2.PdfReader(filehandle)
                    pagehandle = pdfReader.pages[0]
                    text = pagehandle.extract_text()
                    text = text.replace('o','')
                    text = text.replace('|','')
                    # print(text)

                    annotations = skill_extractor.annotate(text)
                    allresult =annotations['results']
                    allresult.keys()
                    
                    fullmatches = allresult['full_matches']
                    ngrams_scored = allresult['ngram_scored']
                    a_key = "doc_node_value"

                    f_docnodevalues = [a_dict[a_key] for a_dict in fullmatches]
                    n_docnodevalues = [a_dict[a_key] for a_dict in ngrams_scored]

                    all_doc_node_values = f_docnodevalues + n_docnodevalues
                    cleaned_values = list(set(all_doc_node_values)) 
                    # print(cleaned_values)

                    scraped_data = [' '.join(cleaned_values)]
                    cv = [' '.join(sanitized_values)]
                    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
                    tfidf_jobid = tfidf_vectorizer.fit_transform(scraped_data)
                    user_tfidf = tfidf_vectorizer.transform(cv)
                    cos_similarity_tfidf = cosine_similarity(user_tfidf, tfidf_jobid)
                    similarity_score = round(np.max(cos_similarity_tfidf), 2)

                    if similarity_score == 0.0:
                        similarity_score = -1.0


                   
                    # print(cleaned_values)
                applicants[candidate_id] = {'ExtractedSkill': cleaned_values,'application_id': application_id,'required_skills':sanitized_values,'Similarity_scores':similarity_score}
                sorted_applicants = sorted(applicants.items(),key=lambda x:x[1]['Similarity_scores'],reverse=True)
                
                rank = 1
                for i, (candidate_id, application_details) in enumerate(sorted_applicants):
                 
                    application_details['rank'] = rank
                    ranked_applicants.append((candidate_id, application_details))
                   
                    if i < len(sorted_applicants) - 1 and application_details['Similarity_scores'] != sorted_applicants[i+1][1]['Similarity_scores']:
                        rank += 1
            # print(ranked_applicants)
            for k in ranked_applicants:
                candidate_id = k[0]
                if candidate_id not in seen_candidate_ids :
                    seen_candidate_ids.add(candidate_id)
                    unique_ranked_applicants.append(k)

            print(unique_ranked_applicants)


        else:
            applications = Applylist.objects.filter(job__in=jobs).order_by('applieddate')

        # Get the value of the select element
        sort_by = request.GET.get('sort_by')
        
        # Sort the queryset based on the selected option
        if sort_by == 'oldest':
            applications = Applylist.objects.filter(job__in=jobs, job__jobname=jobname_filter).order_by('applieddate')
        
        paginator = Paginator(applications, 10)
        page = request.GET.get('page')
        applications = paginator.get_page(page)

        # Get the applicants for each application
        applicants = []
        # print(ranked_applicants)
        for application in applications:
            applicants_query = Applicants.objects.filter(job=application.job, applicant=application.cand)
            applicants.append(applicants_query)
        
        context = {'Apply': applications, 'applicants': applicants, 'jobs': jobs,'rankedapplicants':unique_ranked_applicants}
    return render(request, "Comp/Applylist.html", context)



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



@login_required
def AddVideo(request):
    form=VideoForm()
    if request.method=='POST':
        form=VideoForm(request.POST,request.FILES)
        if form.is_valid():
            title=form.cleaned_data['title']
            desp=form.cleaned_data['desp']
            course=form.cleaned_data['course']
            video=form.cleaned_data['video']
            Videos.objects.create(title=title,slug=slugify(title),desp=desp,course=course,video=video).save()
            return redirect("Companyhome")
    return render(request,"Courses/Add_Video.html",{"form":form})



@login_required
def edit_video(request, id):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_company:
            video = get_object_or_404(Videos, id=id, course__userid=user)
            if request.method == 'POST':
                form = VideoForm(request.POST, request.FILES, instance=video)
                print(video)
                if form.is_valid():
                    form.save()
                    return redirect('recruiter_videos')
            else:
                form = VideoForm(instance=video)
    return render(request, 'Courses/Editvedio.html', {'form': form})

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

from nltk.sentiment import SentimentIntensityAnalyzer

def viewfeedback(request):
    user = Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated and request.user.is_company:
        ins = Account.objects.filter(id=request.user.id)
        course = Courses.objects.get(userid=request.user.id)
        feed = Feedback.objects.filter(course_id=course.id)
        std_ids = feed.values_list("userid", flat=True)
        std = Account.objects.filter(id__in=std_ids)
        
        # Perform sentiment analysis on each feedback comment
        sid = SentimentIntensityAnalyzer()
        sentiment_scores = []
        for f in feed:
            score = sid.polarity_scores(f.feedback)
            sentiment_scores.append(score)
            # Add the sentiment score to the Feedback model
            f.sentiment_score = score['compound']
            f.save()
        
        # Combine feedback objects with their corresponding sentiment scores and student accounts
        std_feed = zip(feed, sentiment_scores, std)
        
        return render(request, 'Comp/viewfeedback.html', {'ins': ins, 'std_feed': std_feed})
    


def note(request, id):
    if request.user.is_authenticated and request.user.is_company:
        user = get_object_or_404(Account, email=request.session.get('email'))
        apply = get_object_or_404(Applylist, id=id, job__email=user)
        if request.method == "POST":
            note = request.POST.get('note')
            apply.recruiter_notes = note
            apply.save()

            # Send email to the candidate
            candidate_email = apply.cand.email
            subject = "Recruiter Note for Job Application"
            message = f"Dear {apply.cand.username},\n\nYou have received a note from the recruiter regarding your job application:\n\n{note}\n\nBest regards,\nThe Recruiter"
            job = apply.job
            sender_email = job.email.email  # Use the recruiter's email address from the JobDetails model
            send_mail(subject, message, sender_email, [candidate_email], fail_silently=False)

    return redirect('Applylist')  # Replace 'applylist' with the appropriate URL name



from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404
from django.contrib import messages

from .models import Applicants

def update_application_status(request, id):
    try:
        application = Applylist.objects.get(id=id)
    except Applylist.DoesNotExist:
        raise Http404("Application does not exist")

    if request.method == 'POST':
        status = request.POST.get('status')
        application.status = status
        application.save()

        messages.success(request, 'Application status updated successfully.')
        # Redirect to the current page
        return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'application': application
    }
    return render(request, 'Comp/Applylist.html', context)


from Employee.models import Videos

def recruiter_videos(request):
    user = Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated and request.user.is_company:
     videos = Videos.objects.filter(course__userid=user)
     print(videos)
     context = {'videos': videos}
    return render(request, 'Courses/vediolist.html', context)


def deletevedio(request, id):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_company:
           videos = Videos.objects.get(id=id)
           videos.delete()
    return redirect("recruiter_videos")



@login_required(login_url='login')
def viewjob(request, id):
    Job=JobDetails.objects.filter(id=id)
    Job11=JobDetails.objects.get(id=id)
   
    
    context={
        'Job':Job,
   
    }
    return render(request,'Comp/ViewJob.html',context)  

def list_selected_candidates(request):
    applicants = Applylist.objects.filter(status='SELECTED')
    return render(request, 'Comp/selected_candidates.html', {'applicants': applicants})
    
def schedule_zoom_meeting(applicant_email):
    zoom_client = ZoomClient(api_key=settings.ZOOM_API_KEY, api_secret=settings.ZOOM_API_SECRET)

    # Generate a unique meeting topic based on the applicant's email
    meeting_topic = f"Interview with {applicant_email}"

    # Set up the meeting parameters
    meeting_params = {
        "topic": meeting_topic,
        "type": 1,  # Scheduled meeting
        "start_time": "YYYY-MM-DDTHH:MM:SSZ",  # Replace with the actual start time of the meeting
        "duration": 60,  # Meeting duration in minutes
        "timezone": "UTC",  # Replace with the appropriate timezone
        "password": "123456",  # Replace with a secure password for the meeting
        "agenda": "Interview with the applicant",  # Meeting agenda
        "settings": {
            "host_video": False,  # Disable host video
            "participant_video": True,  # Enable participant video
            "join_before_host": False,  # Participants cannot join before the host
        }
    }

    # Create the Zoom meeting
    response = zoom_client.meeting.create(data=meeting_params)

    if response['status'] == 'success':
        meeting_id = response['response']['id']
        join_url = response['response']['join_url']
        start_url = response['response']['start_url']
        return meeting_id, join_url, start_url
    else:
        return None, None, None

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from .utils import schedule_zoom_meeting

def interview_schedule(request, id):
    # Get the selected applicant using the provided id
    applicant = Applylist.objects.get(id=id)

    if request.method == "POST":
        # Schedule a Zoom meeting for the applicant
        meeting_id, join_url, start_url = schedule_zoom_meeting(applicant.cand.email)

        if meeting_id and join_url and start_url:
            # Update the Applylist object with the Zoom meeting details
            applicant.zoom_meeting_id = meeting_id
            applicant.zoom_join_url = join_url
            applicant.zoom_start_url = start_url
            applicant.save()

            # Send the interview link to the candidate via email
            subject = "Interview Invitation"
            message = f"Dear {applicant.cand.username},\n\nYou have been invited for an interview. Here is the Zoom meeting link:\n\n{applicant.zoom_join_url}\n\nBest regards,\nRecruiter"
            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [applicant.cand.email]
            html_message = f"<p>Dear {applicant.cand.username},</p><p>You have been invited for an interview. Here is the Zoom meeting link:</p><p><a href='{applicant.zoom_join_url}'>Join the Zoom Meeting</a></p><p>Best regards,<br>Recruiter</p>"

            send_mail(subject, message, from_email, recipient_list, html_message=html_message, fail_silently=False)

            # Perform any additional actions or redirect as needed
            return redirect('Interview_App')  # Redirect to the applicant list page after scheduling the interview
        else:
            # Handle the case when the Zoom meeting creation fails
            pass

    context = {
        'applicant': applicant
    }
    return render(request, 'Comp/interview.html', context)




def Interview_App(request):
    applicants = Applylist.objects.all()
    return render(request, 'Comp/interview.html', {'applicants': applicants})

