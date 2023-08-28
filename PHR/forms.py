from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from PHR.models import *


# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ["username", "email", "password1", "password2"]

	def __init__(self, *args, **kwargs):
		super(NewUserForm, self).__init__(*args, **kwargs)
		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'


class DocumentCategoryMasterForm(forms.ModelForm):
    class Meta:
        model = DocumentCategoryMaster
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(DocumentCategoryMasterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            
class PurposeMasterForm(forms.ModelForm):
    class Meta:
        model = PurposeMaster
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(PurposeMasterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class HospitalMasterForm(forms.ModelForm):
    class Meta:
        model = HospitalMaster
        fields='__all__'
    def __init__(self, *args, **kwargs):
        super(HospitalMasterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
