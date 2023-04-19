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


#to view the resume
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






#to view as pdf
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


#to view all the resume and manage them
def manage_resumes(request):
   
    data1=resumme.objects.filter(user_id = request.user.id)
    return render(request,'Resume/Manage_Resume.html',{'data1':data1})




# to delete a resume
@login_required
def resume_delete(request, res_id):
    r = resumme.objects.get(res_id=res_id)
  
    r.delete()

    return redirect("manage_resumes")





# to get resume details from the user
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
            return redirect('manage_resumes')

#to add internship details
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


#to add project details
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


#to add achievements details
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



# to add certificate details
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