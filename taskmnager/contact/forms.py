from django import forms
from .models import Contact



class ContactForm(forms.ModelForm):

    captcha = ReCapthaFiled()

    class Meta:
        model = Contact
        fields = ('email', )
        widgets = {
            "email": forms.TextInput(attrs={"class": "editContent"})
        }