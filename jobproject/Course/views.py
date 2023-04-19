from datetime import date, timedelta

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.http import HttpResponse
from django.utils.text import slugify
from hashlib import sha256

from django.http import HttpResponseRedirect


from django.db.models import Q
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.template.loader import render_to_string


from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

from django.core.paginator import Paginator, EmptyPage,InvalidPage
from matplotlib import pyplot as plt
from Account.models import Account
from Employee.models import  Courses, Course_purchase,Videos,Feedback,Payment
import razorpay

from jobproject.settings import RAZORPAY_API_KEY

@login_required(login_url='login')
def coursesenrolled(request):
    c = Course_purchase.objects.filter(userid=request.user.id).values_list('course_id',flat=True)
    # print(c)
    courses=Courses.objects.filter(id__in=c)
  
    return render(request, 'Courses/coursesenrolled.html', { 'c': courses})



@login_required(login_url='login')
def availablecourses(request):
    user = Account.objects.get(email=request.session.get('email'))
    if request.user.is_employee:
        all_courses = Courses.objects.all()
        paginator = Paginator(all_courses, 5) # Show 5 courses per page
        page_number = request.GET.get('page')
        courses = paginator.get_page(page_number)

        return render(request, 'Courses/availablecourses.html', {'courses': courses, 'user': user})





@login_required(login_url='login')
def Course_endroll(request,c_slug):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
    c = Courses.objects.get(slug=c_slug)
    endroll=Course_purchase(course_id=c.id,userid=user,end_date=c.end_date)
    endroll.save()
    return redirect("coursesenrolled")




@login_required(login_url='login')
def feedback(request):
   user=Account.objects.get(email=request.session.get('email'))
   if request.user.is_employee:
    c = Course_purchase.objects.filter(userid=user).values_list('course_id',flat=True)
    print(list(c))
    courses=Courses.objects.filter(id__in=c)
    if request.method == "POST":
        feedback= request.POST['feedback']
        course = request.POST['course']
        selected_course=Courses.objects.get(id=course)
        f = Feedback(userid=user,feedback=feedback,course=selected_course)
        f.save()
        return redirect("coursesenrolled")
    return render(request, 'Courses/feedback.html',{"c":courses})
   


@login_required(login_url='login')
def Course_cancel(request,course_id):
    id = request.user.id
    course=get_object_or_404(Course_purchase,course_id=course_id,id=id)
    course.delete()
    return redirect("Course/coursesenrolled")



from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob


# def sentiment_analysis(request):
#     feedback = Feedback.objects.get(id=id)
#     blob = TextBlob(feedback.feedback)
#     positive_percentage = round(blob.sentiment.polarity * 100, 2)
#     negative_percentage = round(100 - positive_percentage, 2)
#     neutral_percentage = 100 - positive_percentage - negative_percentage
#     compoud_score = round(blob.sentiment.subjectivity * 100, 2)

#     # Update sentiment model with new data
#     sent_obj, created = sentiment.objects.get_or_create(review=feedback)
#     sent_obj.positive_percentage = positive_percentage
#     sent_obj.negative_percentage = negative_percentage
#     sent_obj.neutral_percentage = neutral_percentage
#     sent_obj.compoud_score = compoud_score
#     sent_obj.num_reviews += 1
#     sent_obj.save()

#     return render(request, 'Comp/viewfeedback.html', {'feedback': feedback, 'sentiment': sent_obj})








@login_required(login_url='login')
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
              paginator=Paginator(videos,3)     # 10 videos per page
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

   


from datetime import date, datetime

def checkoutcourse(request, c_slug):
    user = Account.objects.get(email=request.session.get('email'))
    course = get_object_or_404(Courses, slug=c_slug)


    razoramount = float(course.amount * 100)

    print(razoramount)
    client = razorpay.Client(auth=(settings.RAZORPAY_API_KEY, settings.RAZORPAY_API_SECRET_KEY))
    data = {
        "amount": razoramount,
        "currency": "INR",
        "receipt": "order_rcptid_11"}
    payment_response = client.order.create(data=data)
    print(payment_response)
    order_id = payment_response['id']
    request.session['order_id'] = order_id
    order_status = payment_response['status']
    if order_status == 'created':
        payment = Payment(user_id=request.user.id,
                          amount=razoramount,
                          razorpay_order_id=order_id,
                          razorpay_payment_status=order_status)
        payment.save()
    request.session['course_id'] = course.id
    context = {
        'course': course,
        'user':user,
        'razoramount': razoramount
    }
    return render(request, 'Courses/checkout.html', context)

def payment_done_course(request):
    order_id = request.session['order_id']
    payment_id = request.GET.get('payment_id')
    print(payment_id)

    payment = Payment.objects.get(razorpay_order_id=order_id)

    payment.paid = True
    payment.razorpay_payment_id = payment_id
    payment.course = Courses.objects.get(id=request.session['course_id'])
    payment.save()

    user =  Account.objects.get(email=request.session.get('email'))
    course = payment.course.id
    purchase_date = datetime.now().date()
    end_date = purchase_date + timedelta(days=30)  # or any other duration you want to set
    course_purchase = Course_purchase(userid=user, course_id=course, purhase_date=purchase_date, end_date=end_date)
    course_purchase.save()


    return redirect('availablecourses')
