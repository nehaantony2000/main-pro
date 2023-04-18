from django.template import Context, Template, loader 
from fileinput import filename
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect,reverse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from Account.models import Account
from .models import *
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def res(request):
        iid = request.POST.get('iid', None)  # Use request.POST.get() with a default value of None
        data1 = resumme.objects.filter(res_id=iid)
        data2 = interdetails.objects.filter(cann_id=request.user.id)
        data3 = projectdetails.objects.filter(cann_id=request.user.id)
        data4 = achidetails.objects.filter(cann_id=request.user.id)
        data5 = certidetails.objects.filter(cann_id=request.user.id)
        return render(request, 'Resume/res.html', {'data1': data1, 'data2': data2, 'data3': data3, 'data4': data4, 'data5': data5})
  
def resdetails(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_employee:
            return render(request,'Resume/del.html')
    return redirect('userhome')




# def resubmit(request):
#     # Get the current user's resume (if it exists)
#     try:
#         user = resume.objects.get(user_id=request.user.id)
#     except resume.DoesNotExist:
#         user = None

#     if user:
#         # Update the existing resume
     
#         user.position = request.POST['pos']
#         user.carobj = request.POST['co']
#         user.email = request.POST['email']
#         user.college = request.POST['col']
#         user.plus = request.POST['plus']
#         user.ten = request.POST['scho']
#         user.projects = request.POST['pro']
#         user.certi = request.POST['certi']
#         user.achi = request.POST['achi']
#         user.interns = request.POST['intern']
#         user.refe = request.POST['ref']
#         user.address = request.POST['address']
#         user.strength = request.POST['stre']
#         user.skills = request.POST['skills']
#         user.lang = request.POST['lang']
#         user.hob = request.POST['hob']
#         user.soci = request.POST['soli']
#         user.coun = request.POST['country']
#         user.dob = request.POST['dob']
#         user.gender = request.POST['gen']
#         user.save()
#     else:
#         # Create a new resume for the user
#         username = request.POST['username']
#         pos = request.POST['pos']
#         co = request.POST['co']
#         email = request.POST['email']
#         col = request.POST['col']
#         plus = request.POST['plus']
#         scho = request.POST['scho']
#         pro = request.POST['pro']
#         certi = request.POST['certi']
#         achi = request.POST['achi']
#         intern = request.POST['intern']
#         ref = request.POST['ref']
#         address = request.POST['address']
#         stre = request.POST['stre']
#         skills = request.POST['skills']
#         lang = request.POST['lang']
#         hob = request.POST['hob']
#         soli = request.POST['soli']
#         country = request.POST['country']
#         dob = request.POST['dob']
#         gen = request.POST['gen']
#         user_id = request.user
#         userr = resume.objects.create(name=username, position=pos, email=email, carobj=co, college=col, plus=plus, ten=scho, projects=pro, certi=certi, achi=achi, interns=intern, refe=ref, address=address, strength=stre, skills=skills, lang=lang, hob=hob, soci=soli, coun=country, dob=dob, gender=gen, user_id=user_id)
#         userr.save()
#     return redirect('res')


import os
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib.staticfiles import finders
from xhtml2pdf import pisa
from io import BytesIO

from django.shortcuts import render
def my_view(request):
    # Retrieve data from the database
            iid=request.POST['iid']
            data1=resumme.objects.filter(res_id = iid)
            data2=interdetails.objects.filter(cann_id = request.user.id)
            data3=projectdetails.objects.filter(cann_id = request.user.id)
            data4=achidetails.objects.filter(cann_id = request.user.id)
            data5=certidetails.objects.filter(cann_id = request.user.id)
           
    # Render an HTML template using the retrieved data
            template = get_template('Resume/res.html')
            html = template.render({'data1': data1,'data2': data2,'data3': data3,'data4': data4,'data5': data5})

            # Generate a PDF from the HTML using xhtml2pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="my_pdf.pdf"'

            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('Error generating PDF file')
            return response



def manage_resumes(request):
   
    data1=resumme.objects.filter(user_id = request.user.id)
    return render(request,'Resume/Manage_Resume.html',{'data1':data1})





@login_required
def resume_delete(request, res_id):
    r = resumme.objects.get(res_id=res_id)
  
    r.delete()

    return redirect("manage_resumes")






def resubmit(request):
    user = Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_employee:
            username = request.POST.get('username')
            pos = request.POST.get('pos')
            co = request.POST.get('co')
            email = request.POST.get('email')
            col = request.POST.get('col')
            colcourse = request.POST.get('colcourse')
            colpy = request.POST.get('colpy')
            plus = request.POST.get('plus')
            plusmarks = request.POST.get('plusmarks')
            pluspy = request.POST.get('pluspy')
            scho = request.POST.get('scho')
            schomarks = request.POST.get('schomarks')
            schopy = request.POST.get('schopy')
            ref = request.POST.get('ref')
            phone = request.POST.get('phone')
            address = request.POST.get('address')
            stre = request.POST.get('stre')
            skills = request.POST.get('skills')
            lang = request.POST.get('lang')
            hob = request.POST.get('hob')
            soli = request.POST.get('soli')
            country = request.POST.get('country')
            dob = request.POST.get('dob')
            gen = request.POST.get('gen')
            uid = request.POST.get('uid')

            # Get the Account instance for the user
            user_account = Account.objects.get(id=request.user.id)

            userr = resumme(
                name=username,
                position=pos,
                email=email,
                carobj=co,
                college=col,
                plus=plus,
                ten=scho,
                refe=ref,
                phone=phone,
                address=address,
                strength=stre,
                skills=skills,
                lang=lang,
                hob=hob,
                soci=soli,
                coun=country,
                dob=dob,
                gender=gen,
                user_id=user_account,  # Pass the Account instance for user_id
                colcourse=colcourse,
                colpy=colpy,
                plusmarks=plusmarks,
                pluspy=pluspy,
                schomarks=schomarks,
                schopy=schopy
            )
            print(userr)
            userr.save()
            print(userr)
            return redirect('res')


def interdetail(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_employee:
            interns=request.POST['interns']
            internname=request.POST['internname']
            interndate=request.POST['interndate']
            member = interdetails(cann_id=request.user.id,interns=interns,internname=internname,interndate=interndate)
            member.save()
            return redirect('resdetails')
        return redirect('userhome')

def projectdetail(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_employee:
            proname=request.POST['proname']
            prodetails=request.POST['prodetails']
            member = projectdetails(cann_id=request.user.id,proname=proname,prodetails=prodetails)
            member.save()
            return redirect('resdetails')
    return redirect('userhome')

def achidetail(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_employee:
            achiname=request.POST['achiname']
            achiinfo=request.POST['achiinfo']
            achidate=request.POST['achidate']
            member = achidetails(cann_id=request.user.id,achiname=achiname,achiinfo=achiinfo,achidate=achidate)
            member.save()
            return redirect('resdetails')
    return redirect('userhome')

def certidetail(request):
    user=Account.objects.get(email=request.session.get('email'))
    if request.user.is_authenticated:
        if request.user.is_employee:
            certiname=request.POST['certiname']
            cerinfo=request.POST['cerinfo']
            certidate=request.POST['certidate']
            member = certidetails(cann_id=request.user.id,certiname=certiname,cerinfo=cerinfo,certidate=certidate)
            member.save()
            return redirect('resdetails')
    return redirect('userhome')