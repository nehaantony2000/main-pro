
from fileinput import filename
from django.http import HttpResponse, JsonResponse, response
from django.shortcuts import render, redirect,reverse
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from Account.models import Account
from Employee.models import resume


def res(request):
    data1=resume.objects.filter(user_id = request.user.id)
    context={
        'data1':data1
    }
    return render(request,'Resume/res.html',context)

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
    phone= request.POST['phone']
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
    userr = resume(name=username,position=pos,email=email,carobj=co,college=col,plus=plus,ten=scho,projects=pro,certi=certi,achi=achi,interns=intern,refe=ref,phone=phone,address=address,strength=stre,skills=skills,lang=lang,hob=hob,soci=soli,coun=country,dob=dob,gender=gen,user_id=uid)
    userr.save()
    return redirect('res')