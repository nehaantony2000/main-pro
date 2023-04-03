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
    # Get the current user's resume (if it exists)
    try:
        user = resume.objects.get(user_id=request.user.id)
    except resume.DoesNotExist:
        user = None

    if user:
        # Update the existing resume
     
        user.position = request.POST['pos']
        user.carobj = request.POST['co']
        user.email = request.POST['email']
        user.college = request.POST['col']
        user.plus = request.POST['plus']
        user.ten = request.POST['scho']
        user.projects = request.POST['pro']
        user.certi = request.POST['certi']
        user.achi = request.POST['achi']
        user.interns = request.POST['intern']
        user.refe = request.POST['ref']
        user.address = request.POST['address']
        user.strength = request.POST['stre']
        user.skills = request.POST['skills']
        user.lang = request.POST['lang']
        user.hob = request.POST['hob']
        user.soci = request.POST['soli']
        user.coun = request.POST['country']
        user.dob = request.POST['dob']
        user.gender = request.POST['gen']
        user.save()
    else:
        # Create a new resume for the user
        username = request.POST['username']
        pos = request.POST['pos']
        co = request.POST['co']
        email = request.POST['email']
        col = request.POST['col']
        plus = request.POST['plus']
        scho = request.POST['scho']
        pro = request.POST['pro']
        certi = request.POST['certi']
        achi = request.POST['achi']
        intern = request.POST['intern']
        ref = request.POST['ref']
        address = request.POST['address']
        stre = request.POST['stre']
        skills = request.POST['skills']
        lang = request.POST['lang']
        hob = request.POST['hob']
        soli = request.POST['soli']
        country = request.POST['country']
        dob = request.POST['dob']
        gen = request.POST['gen']
        user_id = request.user
        userr = resume.objects.create(name=username, position=pos, email=email, carobj=co, college=col, plus=plus, ten=scho, projects=pro, certi=certi, achi=achi, interns=intern, refe=ref, address=address, strength=stre, skills=skills, lang=lang, hob=hob, soci=soli, coun=country, dob=dob, gender=gen, user_id=user_id)
        userr.save()
    return redirect('res')


import os
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib.staticfiles import finders
from xhtml2pdf import pisa
from io import BytesIO

from django.shortcuts import render

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Build the path to the CSS file
css_path = os.path.join(BASE_DIR, 'static', 'new', 'css', 'style.css')

# Load the CSS file
with open(css_path, encoding='utf-8') as f:
    css = f.read()

def my_view(request):
    # Retrieve data from the database
    data1 = resume.objects.filter(user_id=request.user.id)
    data2 = request.user.profilepic
    
    # Render an HTML template using the retrieved data and CSS
    template = get_template('Resume/res.html')
    context = {'data1': data1, 'data2': data2, 'css': css}

    html = template.render(context)

    # Generate a PDF from the HTML using xhtml2pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="my_pdf.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF file')
    return response




def manage_resumes(request):
   
    resumes = resume.objects.filter(user_id=request.user.id)

    return render(request, 'Resume/Manage_Resume.html', {'resumes': resumes})




@login_required
def resume_delete(request, res_id):
    r = resume.objects.get(res_id=res_id)
  
    r.delete()

    return redirect("manage_resumes")