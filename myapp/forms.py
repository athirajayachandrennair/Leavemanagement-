from django import forms
from .models import crud

from .models import add
from .models import users

class AddForm(forms.ModelForm):
    class Meta:
        model = crud



        fields = ('name','age','email','address')

        widgets={

            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            # 'image':forms.FileInput(attrs={'class':'form-control'}),
            
        }



class regform(forms.ModelForm):
    class Meta:
        model = add
        fields = ('firstname','lastname','email','phonenumber','username','password')
        widgets={

            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'}),
           
        }

class AddForm1(forms.ModelForm):
    class Meta:
        model = users
        fields = ('username','password')

        widgets={

            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }