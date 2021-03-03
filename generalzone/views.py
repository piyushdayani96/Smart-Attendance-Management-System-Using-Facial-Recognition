from django.shortcuts import render,redirect,reverse
from django.core.exceptions import ObjectDoesNotExist
from .models import LoginInfo,StudentInfo,Enquiry
from .forms import *
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import datetime
def index(request):
    return render(request,'index.html')
# Create your views here..
def about(request):
    return render(request,'about.html')
def registration(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            rollno = form.cleaned_data['rollno']
            password = form.cleaned_data['password']
            li = LoginInfo(userid=rollno, password=password, usertype='student')
            li.save()
            form.instance.file.name=str(rollno)+".jpg"
            form.save()

            return redirect('registration.html')
    else:
        form = DocumentForm()
    return render(request, 'registration.html', {'form': form})
   # return render(request,'registration.html')
def login(request):
    return render(request,'login.html')
def enquiry(request):
    return render(request,'enquiry.html')
def validateuser(request):
    userid=request.POST['userid']
    password=request.POST['password']
    try:
        v=LoginInfo.objects.get(userid=userid,password=password)
        if v is not None:
            usertype=v.usertype
            if usertype=='student':
                request.session['userid']=userid
                return redirect(reverse('studentzone:userzone'))
            elif usertype=='teacher':
                request.session['teachid']=userid
                return redirect(reverse('teachers:home'))
            elif usertype=='director':
                request.session['direcid']=userid
                return redirect(reverse('director:direchome'))
    except ObjectDoesNotExist:
        return redirect('index')
def stureg(request):
    '''name=request.POST['name']
    rollno=request.POST['rollno']
    gender=request.POST['gender']
    address=request.POST['address']
    nationality=request.POST['nationality']
    contactno=request.POST['contactno']
    emailaddress=request.POST['email']
    password=request.POST['password']
    connectdate=datetime.datetime.now().strftime('%Y/%m/%d')
    usertype='student'
    if StudentInfo.objects.filter(rollno=rollno).exists():
        msg='Student is already Registered'
    else:
        ci = StudentInfo(name=name, gender=gender,rollno=rollno, address=address, nationality=nationality, contactno=contactno,
                         emailaddress=emailaddress, password=password, connectdate=connectdate)
        li = LoginInfo(userid=rollno, password=password, usertype=usertype)
        ci.save()
        li.save()
        msg='Registration is Done.'
    return render(request,'registration.html',{'msg':msg})
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return redirect('registration.html')
    else:
        form = DocumentForm()
    return render(request, 'registration.html', {'form': form})'''

def enquiry(request):
    return render(request,'enquiry.html')
def saveenquiry(request):
    name=request.POST['name']
    gender=request.POST['gender']
    address=request.POST['address']
    contactno=request.POST['contactno']
    emailaddress=request.POST['emailaddress']
    enquirytext=request.POST['enquirytext']
    enquirydate=datetime.datetime.now().strftime("%Y/%m/%d")
    en=Enquiry(name=name,gender=gender,address=address,contact_no=contactno,emailaddress=emailaddress,enquirytext=enquirytext,enquirydate=enquirydate)
    en.save()
    return redirect('index')