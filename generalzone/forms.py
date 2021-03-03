from django import forms
import datetime
from .models import StudentInfo
from director.models import Department
GENDER = (
   ('Male', 'Male'),
   ('Female', 'Female'),
)
class DocumentForm(forms.ModelForm):
    gender= forms.ChoiceField(choices=GENDER, widget=forms.RadioSelect())
    branch=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control col-sm-6'}))
    branch.choices=[(department.deptname,department.deptname) for department in Department.objects.all()]
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control col-sm-6'}))
    class Meta:
        model = StudentInfo
        connectdate = datetime.datetime.now().strftime('%Y/%m/%d')
       # datee=datetime.datetime.now().strftime('%Y/%m/%d')
        fields = ('name','gender','rollno', 'address', 'branch','contactno',
                         'emailaddress', 'password','file', )
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control col-sm-6'}),
            'contactno': forms.TextInput(attrs={'class':'form-control col-sm-6'}),
            'rollno': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
            'contactno': forms.TextInput(attrs={'class': 'form-control col-sm-6'}),
            'password':forms.PasswordInput(attrs={'class':'form-control col-sm-6'}),
            'file':forms.FileInput(attrs={'class':'form-control col-sm-6'}),
            'emailaddress':forms.TextInput(attrs={'class':'form-control col-sm-6'}),
        }