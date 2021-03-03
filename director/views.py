from django.shortcuts import render,redirect,reverse
from .models import Department,Subject
from generalzone.models import LoginInfo
def direchome(request):
    if (request.session['direcid']):
        dept=Department.objects.all()
        return render(request,'home1.html',{'dept':dept})
    else:
        return render(request,'index.html')
# Create your views here.
def createtable(request):
    if(request.session['direcid']):
        return render(request,'createtable.html')
    else:
        return render(request,'index.html')
def savetable(request):
    if(request.session['direcid']):
        deptname=request.POST['deptname']
        deptcode=request.POST['deptcode']
        depthod=request.POST['depthod']
        course=request.POST['course']
        re=Department(deptname=deptname,deptcode=deptcode,depthod=depthod,course=course)
        re.save()
        return redirect('director:direchome')
    else:
        return render(request,'index.html')
def deletedepartment(request,id):
    if request.session['direcid']:
        e=Department.objects.get(id=id)
        e.delete()
        return redirect('director:direchome')
    else:
        return render(request,'index.html')
def createsubject(request):
    if request.session['direcid']:
        x=LoginInfo.objects.filter(usertype='teacher')
        y=Department.objects.all()
        context={'x':x,'y':y}
        return render(request,'createsubject.html',context)
    else:
        return render(request,'index.html')
def savesubject(request):
    if request.session['direcid']:
        subjectname=request.POST['subjectname']
        deptname=request.POST['deptname']
        semester=request.POST['semester']
        subjectcode=request.POST['subjectcode']
        teachername=request.POST['teachername']
        de=Subject(subjectname=subjectname,dept=deptname,semester=semester,subjectcode=subjectcode,teachername=teachername)
        de.save()
        e = Department.objects.get(deptname=deptname)
        return redirect('director:showsubject',e.id)
    else:
        return render(request,'index.html')
def showsubject(request,id):
    if request.session['direcid']:
          e=Department.objects.get(id=id)
          ss=Subject.objects.filter(dept=e.deptname)
          p=''
          if(e.deptname=="CSE"):
              p='Computer Science & Engineering'
          elif(e.deptname=="EE"):
              p="Electrical Engineering"
          elif(e.deptname=="EL"):
              p="Electronic Engineering"

          return render(request,'showsubject.html',{'ss':ss,'p':p})
    else:
        return render(request,'index.html')



