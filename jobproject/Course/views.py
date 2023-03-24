from datetime import date

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.utils.text import slugify
from hashlib import sha256


from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string




from django.core.paginator import Paginator, EmptyPage,InvalidPage
from Account.models import Account
from Employee.models import  Courses, Course_purchase,Videos
@login_required
def coursesenrolled(request):
    c = Course_purchase.objects.filter(userid=request.user.id).values_list('course_id',flat=True)
    # print(c)
    courses=Courses.objects.filter(id__in=c)
    return render(request, 'Courses/coursesenrolled.html', { 'c': courses})



@login_required
def availablecourses(request):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
    c = Courses.objects.all()
    return render(request, 'Courses/availablecourses.html', {'c': c, 'user': user})




@login_required
def Course_endroll(request,c_slug):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
    c = Courses.objects.get(slug=c_slug)
    endroll=Course_purchase(course_id=c.id,userid=user,end_date=c.end_date)
    endroll.save()
    return redirect("Course/coursesenrolled")


# def feedback(request):

#     c = Course_purchase.objects.filter(user_id=request.user.id).values_list('course_id',flat=True)
#     print(list(c))
#     courses=Courses.objects.filter(id__in=c)
#     if request.method == "POST":
#         feedback= request.POST['feedback']
#         course = request.POST['course']
#         selected_course=Courses.objects.get(id=course)
#         f = Feedback(user_id=request.user.id,feedback=feedback,course=selected_course)
#         f.save()
#     return render(request, 'Course/feedback.html',{"c":courses})

# def AddVideo(request):
#     form=VideoForm()
#     if request.method=='POST':
#         form=VideoForm(request.POST,request.FILES)
#         if form.is_valid():
#             title=form.cleaned_data['title']
#             course=form.cleaned_data['course']
#             video=form.cleaned_data['video']
#             Videos(title=title,slug=slugify(title),course=course,video=video).save()
#             return redirect("Cinstructordashboard")
#     return render(request,"Course/Add_Video.html",{"form":form})
@login_required
def Course_cancel(request,course_id):
    id = request.user.id
    course=get_object_or_404(Course_purchase,course_id=course_id,id=id)
    course.delete()
    return redirect("Course/coursesenrolled")



@login_required
def playcourse(request,c_slug=None,v_slug=None):
   std=Account.objects.get(email=request.session.get('email'))
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
                
                 return render(request, 'Courses/playcourse.html',{"c_videos":videos,"video_key": video,"std":std})

              return render(request, 'Courses/playcourse.html',{"c_videos":videos,"std":std})

            else:
                id=request.user.id
                courses=Courses.objects.all()
                std=Account.objects.get(email=request.session.get('email'))
                return render(request,'Courses/playcourse.html',{'std':std,'courses':courses})

   



