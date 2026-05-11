from django import forms
from .models import StudentProfileModel
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfileModel
        fields=('name','age','gender','studentClass','phoneNo','email')

    def __init__(self, *args, **kwargs):
        super(StudentProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'