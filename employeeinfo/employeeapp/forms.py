from django import forms
from .models import Employee

class Employeeform(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['ename', 'egender', 'eage', 'email','esalary','doj', 'eyoe','edep','company','profile']

        widgets={
            'doj':forms.DateInput(attrs={
                'class':'form-control','type':'date'
            }),
            'egender':forms.Select(attrs={
                'class':'form-control'
        })
        }