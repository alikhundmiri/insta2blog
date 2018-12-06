from django import forms
from django.contrib.auth.models import User as User_
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)

from . models import insta_account

import re

# from core.models import Profile
User = get_user_model()

class UserLoginForm(forms.Form):
    username = forms.CharField(label='',widget = forms.TextInput(attrs={'placeholder': 'User Name', 'class':'form-control'}))
    password = forms.CharField(label='',widget = forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user does not exist.")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password.")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer Active.")
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(label='',widget = forms.TextInput(attrs={'placeholder': 'User Name', 'class':'form-control'}))
    email = forms.EmailField(label='',widget = forms.TextInput(attrs={'placeholder': 'Email Address', 'class':'form-control'}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class':'form-control'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email has already been registered")
        return email


class InstaIDForm(forms.ModelForm):
    insta_id = forms.CharField(label='Instagram ID',widget = forms.TextInput(attrs={'placeholder': 'Your Instagram ID here', 'class':'form-control'}))

    class Meta:
        model = insta_account
        fields = [
            'insta_id'
        ]
    def clean_insta(self):
        id_ = self.cleaned_data.get('insta_id')
        id_qs = insta_account.objects.filter(insta_id=insta_id)
        if id_qs.exists():
            raise forms.ValidationError("This Instagram account has already been registered.")
        return id_
    


# class ProfileForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = [
#         "avatar",
#         "bio",
#         "profession",
#         "hire_me_if_want",
#         "looking_for",
#         ]

#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)
#         self.fields["bio"].help_text = "A brief description about you are your work or profession in less than 500 words"
#         self.fields["profession"].help_text = "Your Profession! Be creative and go wild, you have a limit of 30 characters"
#         self.fields["hire_me_if_want"].help_text = "List your Specilisations in less than 100 words, example: HTML, CSS, Blockchain, Android App development, VR, AR, etc."
#         self.fields["hire_me_if_want"].label = "Hire me if you want:"
#         self.fields["hire_me_if_want"].widget.attrs['placeholder'] = "Leave blank to hide this on your Portfolio"
        
#         self.fields["looking_for"].help_text = "In less than 100 words. Example: Contract, Full time Job, Part time Job, Freelancing, Remote Worker, Digital Nomad, etc."
#         self.fields["looking_for"].label = "I am looking for:"
#         self.fields["looking_for"].widget.attrs['placeholder'] = "Leave blank to hide this on your Portfolio"
#     def clean_avatar(self):
#         avatar = self.cleaned_data.get('avatar')

#     def clean_bio(self):
#         # print("Validating...")
#         pattern = r'[a-zA-Z0-9 ]'
#         bio = self.cleaned_data.get('bio')
        
#         if not re.search(pattern, bio):
#             # print("Not valid")
#             raise forms.ValidationError("This Bio description contains invalid characters")
#         # print("Valid")
#         return bio
        
#     def clean_profession(self):
#         # print("Validating...")
#         pattern = r'[a-zA-Z0-9 ]'
#         profession = self.cleaned_data.get('profession')
        
#         if not re.search(pattern, profession):
#             # print("Not valid")
#             raise forms.ValidationError("This field contains only invalid characters")
#         # print("Valid")
#         return profession        


# class EditProfileForm(UserChangeForm):
#     class Meta:
#         model = User_
#         fields = (
#             'email',            
#             'first_name',
#             'last_name',
#             'password',
#             )

