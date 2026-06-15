from django import forms
from SchoolApp.models import SchoolProfileModel
from TeacherApp.models import TeacherProfileModel
from StudentApp.models import StudentProfileModel

class SchoolForm(forms.ModelForm):
    class Meta:
        model=SchoolProfileModel
        fields=("__all__")
        exclude=('admin',)
    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class AddStudentSchoolForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super(AddStudentSchoolForm,self).__init__(*args, **kwargs)
        for field_name,field in self.fields.items():
            field.widget.attrs['class']='form-control'
    class Meta:
        model=StudentProfileModel
        fields=('__all__')
        exclude=('user','schoolName')
class AddSchoolTeacherForm(forms.ModelForm):
    class Meta:
        model=TeacherProfileModel
        fields=("__all__")
        exclude=('user',)
    def __init__(self, *args, **kwargs):
        super(AddSchoolTeacherForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'