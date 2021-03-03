from django.shortcuts import render,redirect
from generalzone.models import StudentInfo,LoginInfo
from .models import Question,Answer,Complain
from director.models import Subject
import os
import datetime,openpyxl
import datetime
# Create your views here.
def userzone(request):
    if request.session['userid']:
        x=StudentInfo.objects.get(rollno=request.session['userid'])
        subjectCode=Subject.objects.filter(semester=x.semester)
        now = datetime.datetime.now()
        today = now.day
        month = now.month
        year = now.year
        mn = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
        r =list()
        s=list()
        for p in subjectCode:
            #print(str(p.subjectcode))
            r.append(str(p.subjectcode))
            count=0
            if not os.path.isdir("./media/Attendances/Semester " + str(x.semester) + "/" + str(p.subjectcode) + "/"):
                print(os.makedirs("./media/Attendances/Semester " + str(x.semester) + "/" + str(p.subjectcode) + "/"))
                #print('A')
            for m in mn:
                #print(m)
                #print('A'+str(os.path.isfile(os.path.join("./media/Attendances/Semester " + str(x.semester) + "/" + str(p.subjectcode) + "/",str(m) + '.xlsx'))))
                if os.path.isfile(os.path.join("./media/Attendances/Semester " + str(x.semester) + "/" + str(p.subjectcode) + "/",str(m) + '.xlsx')):
                    #print(os.path.isfile(os.path.join("./media/Attendances/Semester " + str(x.semester) + "/" + str(p) + "/",str(m) + '.xlsx')))
                    wb = openpyxl.load_workbook(
                        os.path.join("./media/Attendances/Semester " + str(x.semester) + "/" + str(p.subjectcode) + "/",
                                     str(m) + '.xlsx'))
                    worksheet = wb.active
                    #print(p.subjectcode)

                    c=0
                    for row in worksheet.iter_rows():
                        #print('X')
                        c=c+1
                        #print(c)
                       # print(row[0])
                        #print(row[0].value)
                        if str(row[0].value)==str(x.rollno):
                                #print('B')
                                if worksheet.cell(row=int(c),column=35).value is not None:
                                    count=count+int(worksheet.cell(row=int(c),column=35).value)
                                    #print('B'+str(count))
            s.append(count)
            #print('C'+str(count))
        return render(request,'userzone.html',{'r':r,'s':s,'subjectCode':subjectCode})
    else:
        return render(request('index.html'))
def discussion(request):
    if request.session['userid']:
        ques = Question.objects.all()
        return render(request, 'discussion.html', {'ques': ques})
    else:
        return render(request('index.html'))
def complainlog(request):
    if request.session['userid']:
        return render(request,'complainlog.html')
    else:
        return render(request('index.html'))
def searchsolution(request):
    if request.session['userid']:
        return render(request,'searchsolution.html')
    else:
        return render(request('index.html'))
def changepassword(request):
    if request.session['userid']:
        return render(request,'changepassword.html')
    else:
        return render(request('index.html'))
def postanswer(request):
    if request.session['userid']:
        rollno=request.session.get('userid')
        student=StudentInfo.objects.get(rollno=rollno)
        answeredby=student.name
        qid=request.POST['qid']
        answertext=request.POST['answertext']
        answereddate=datetime.datetime.now().strftime('%Y/%m/%d')
        a=Answer(answertext=answertext,answeredby=answeredby,qid=qid,answereddate=answereddate)
        a.save()
        return redirect('studentzone:discussion')
    else:
        return render(request,'index.html')

def postquestion(request):
        if request.session['userid']:
            rollno= request.session.get('userid')
            customer = StudentInfo.objects.get(rollno=rollno)
            askedby = customer.name
            questiontext = request.POST['questiontext']
            pasteddate = datetime.datetime.now().strftime('%Y/%m/%d')
            q = Question(questiontext=questiontext, askedby=askedby, pasteddate=pasteddate)
            q.save()
            q=Question.objects.all()
            return render(request, 'discussion.html', {'ques': q})
        else:
            return render(request, 'index.html')
def answer(request,qid):
    if request.session['userid']:
        return render(request,'answer.html',{'qid':qid})
    else:
        return render(request,'index.html')
def viewanswer(request,qid):
    if request.session['userid']:
        ans=Answer.objects.filter(qid=qid)
        return render(request,'viewanswer.html',{'ans':ans})
    else:
        return render(request,'index.html')
def changepwd(request):
    if request.session['userid']:
        userid=request.session.get('userid')
        oldpassword=request.POST['oldpassword']
        newpassword=request.POST['newpassword']
        confirmpassword=request.POST['confirmpassword']
        if newpassword != confirmpassword:
            msg="newpassword and confirmpassword should match"
            return render(request,'changepassword.html',{'msg':msg})
        else:
            user=LoginInfo.objects.get(userid=userid,password=oldpassword)
            if user is not None:
                li=LoginInfo(password=newpassword,userid=userid,usertype='student')
                li.save()
                return render(request,'index.html')
            else:
                msg="old password does not msg"
                return render(request, 'changepassword.html', {'msg': msg})
    else:
        return render(request,'index.html')
def savecomplain(request):
    if request.session['userid']:
        rollno=request.session.get('userid')
        customer=StudentInfo.objects.get(rollno=rollno)
        name=customer.name
        gender=customer.gender
        address=customer.address
        contactno=customer.contactno
        subject=request.POST['subject']
        complaintext=request.POST['complaintext']
        complaindate=datetime.datetime.now().strftime('%Y/%m/%d')
        com=Complain(name=name,gender=gender,address=address,contactno=contactno,subject=subject,complaintext=complaintext,rollno=rollno,complaindate=complaindate)
        com.save()
        return redirect('studentzone:userhome')
    else:
        return render(request,'login.html')
def answer(request,qid):
    if request.session['userid']:
        return render(request,'answer.html',{'qid':qid})
    else:
        return render(request,'login.html')
def postanswer(request):
    if request.session['userid']:
        rollno=request.session.get('userid')
        customer=StudentInfo.objects.get(rollno=rollno)
        answertext=request.POST['answertext']
        qid=request.POST['qid']
        answeredby=customer.name
        answereddate=datetime.datetime.now().strftime('%Y/%m/%d')
        a=Answer(answertext=answertext,answeredby=answeredby,qid=qid,answereddate=answereddate)
        a.save()
        return redirect('studentzone:discussion')
    else:
        return render(request,'login.html')
def viewanswer(request,qid):
    if request.session['userid']:
        ans=Answer.objects.filter(qid=qid)
        return render(request,'viewanswer.html',{'ans':ans})
    else:
        return render(request,'login.html')