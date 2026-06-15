from django import forms
from .models import StudentProfileModel,CourseModel,StudentClass
streamClass=(
    ('XI','XI'),
    ('XII','XII')
)
from django.forms import ModelChoiceField


class StudentProfileForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(StudentProfileForm,self).__init__(*args, **kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs['class']='form-control'
    class Meta:
        model=StudentProfileModel
        fields=('__all__')
        exclude=('user',)
      
     
        

        
            
     
