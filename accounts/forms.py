from typing import Any, Dict
from django import forms


class LoginForm(forms.Form):
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Enter Username" }), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Enter Password"}))

    # def clean_username(self):
    #     return self.cleaned_data['username'][:5] # --> masalan hazf nogte haye ezafe dar akhare input

    # def clean(self) -> Dict[str, Any]:
    #     return super().clean()

class RegisrerForm(forms.Form):

    username= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Enter Username" }), required=True)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Enter Password"}), required=True)
    first_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Enter your first name" }), required=True)
    last_name= forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Enter your last name" }), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Enter a valid email" }))
    bio= forms.CharField(max_length=300 ,widget=forms.TextInput(attrs={'class':'form-control form-control-lg', 'placeholder':"Write a Bio" }), required=True)
    birthdate= forms.DateField(initial="1990-06-21", widget=forms.SelectDateWidget(years=[x for x in range(1940,2024)]), required=False)
    avatar= forms.ImageField(required=False, widget=forms.FileInput())

