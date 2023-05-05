from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={ #ilgili css özellikleri getirildi renk düzeni sebebiyle ekranda gösterilemiyor!!
        'class': 'form-control',
        'placeholder': 'Name',
        'name': 'Name',
        'for' : 'Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={ #ilgili css özellikleri getirildi renk düzeni sebebiyle ekranda gösterilemiyor!!
        'class': 'form-control',
        'placeholder': 'Email',
        'name': 'email',
        'for' : 'email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={ #ilgili css özellikleri getirildi renk düzeni sebebiyle ekranda gösterilemiyor!!
        'class': 'form-control',
        'placeholder': 'Phone',
        'name': 'Phone',
        'for' : 'Phone'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={ #ilgili css özellikleri getirildi renk düzeni sebebiyle ekranda gösterilemiyor!!
        'class': 'form-control',
        'placeholder': 'Message',
        'name': 'Message',
        'for' : 'Message'
    }))

    class Meta:
        model = Contact
        fields = ['name','email','phone','message']