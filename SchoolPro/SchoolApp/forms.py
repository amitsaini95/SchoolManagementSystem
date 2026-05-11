from django import forms
from SchoolApp.models import SchoolProfileModel
class SchoolForm(forms.ModelForm):
    class Meta:
        model=SchoolProfileModel
        fields=("__all__")
        exclude=('admin',)
    def __init__(self, *args, **kwargs):
        super(SchoolForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'