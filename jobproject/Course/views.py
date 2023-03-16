# from datetime import date

# from django.conf import settings
# from django.contrib.auth.decorators import login_required
# from django.contrib.sites.shortcuts import get_current_site
# from django.core.mail import send_mail, EmailMessage
# from django.http import HttpResponse
# from django.utils.text import slugify
# from hashlib import sha256


# from django.db.models import Q
# from django.contrib import messages
# from django.shortcuts import render, redirect, get_object_or_404
# from django.template.loader import render_to_string


# from .forms import VideoForm

# from django.core.paginator import Paginator, EmptyPage,InvalidPage
# from Account.models import Account
# from .models import  Feedback, Videos, Courses, Course_purchase
# def coursesenrolled(request):
#     c = Course_purchase.objects.filter(user_id=request.user.id).values_list('course_id',flat=True)
#     print(list(c))
#     courses=Courses.objects.filter(id__in=c)
#     return render(request, 'Course/coursesenrolled.html', { 'c': courses})




# def availablecourses(request):
#     user = Account.objects.get(user_id=request.user.id)
#     c = Courses.objects.all()
#     return render(request, 'Course/availablecourses.html', {'c': c, 'user': user})





# def Course_endroll(request,c_slug):
#     user = Account.objects.filter(user_id=request.user.id)
#     c = Courses.objects.get(slug=c_slug)
#     endroll=Course_purchase(course_id=c.id,user_id=request.user.id,end_date=c.end_date)
#     endroll.save()
#     return redirect("Employee:coursesenrolled")


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
#             return redirect("Employee:instructordashboard")
#     return render(request,"Course/Add_Video.html",{"form":form})

# def Course_cancel(request,course_id):
#     course=get_object_or_404(Course_purchase,course_id=course_id,user_id=request.user.id)
#     course.delete()
#     return redirect("Employee:coursesenrolled")

