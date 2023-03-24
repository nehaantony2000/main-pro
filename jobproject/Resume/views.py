from django.template import Context, Template, loader 
from fileinput import filename
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect,reverse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from Account.models import Account
from Employee.models import resume
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

def res(request):
    data1=resume.objects.filter(user_id = request.user.id)
    return render(request,'Resume/res.html',{'data1':data1})

def resdetails(request):
    return render(request,'Resume/del.html')

def resubmit(request):
    username= request.POST['username']
    pos= request.POST['pos']
    co= request.POST['co']
    email= request.POST['email']
    col= request.POST['col']
    plus= request.POST['plus']
    scho= request.POST['scho']
    pro= request.POST['pro']
    certi= request.POST['certi']
    achi= request.POST['achi']
    intern= request.POST['intern']
    ref= request.POST['ref']
    address= request.POST['address']
    stre= request.POST['stre']
    skills= request.POST['skills']
    lang= request.POST['lang']
    hob= request.POST['hob']
    soli= request.POST['soli']
    country= request.POST['country']
    dob= request.POST['dob']
    gen= request.POST['gen']
    uid= request.POST['uid']
    userr = resume.objects.create(name=username,position=pos,email=email,carobj=co,college=col,plus=plus,ten=scho,projects=pro,certi=certi,achi=achi,interns=intern,refe=ref,address=address,strength=stre,skills=skills,lang=lang,hob=hob,soci=soli,coun=country,dob=dob,gender=gen,user_id=uid)
    userr.save()
    return redirect('res')




def my_view(request):
    # Retrieve data from the database
            data1=resume.objects.filter(user_id = request.user.id)
            data2=request.user.profilepic
 # Render an HTML template using the retrieved data and CSS
            template = get_template('Resume/res.html')
            context = {'data1': data1, 'data2': data2, 'style': "{% static 'new/css/style.css' %}"}
            html = template.render(context)

            # Generate a PDF from the HTML using xhtml2pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'filename="my_pdf.pdf"'

            pisa_status = pisa.CreatePDF(html, dest=response)
            if pisa_status.err:
                return HttpResponse('Error generating PDF file')
            return response
