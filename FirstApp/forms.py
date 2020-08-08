from django import forms
from FirstApp.models import (Professional_Resources,Personal_Development_Resources,
                             Financial_Success_Resources,MyGoal,MyLibrary,
                             Challenge1,Challenge2,AddExperience,GetAJob,CommentsandSuggestions)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
	       model = User
	       fields = ["username", "email", "password1", "password2"]

class ProfessionalResourcesForm(forms.ModelForm):
    class Meta:
        model=Professional_Resources
        fields='__all__'

class Personal_Development_ResourcesForm(forms.ModelForm):
    class Meta:
        model=Personal_Development_Resources
        fields='__all__'

class Financial_Success_ResourcesForm(forms.ModelForm):
    class Meta:
        model=Financial_Success_Resources
        fields='__all__'

class UserForm(forms.ModelForm):
    password=forms.CharField(max_length=10)

    class Meta():
        model=User
        fields=('username','email','password')

class MyGoalForm(forms.ModelForm):
    class Meta:
        model=MyGoal
        fields="__all__"

class MyLibraryForm(forms.ModelForm):
    class Meta:
        model=MyLibrary
        fields="__all__"

class Challenge2Form(forms.ModelForm):
    class Meta:
        model=Challenge2
        fields="__all__"

class Challenge1Form(forms.ModelForm):
    class Meta:
        model=Challenge1
        fields="__all__"

class AddExperienceForm(forms.ModelForm):
    class Meta:
        model=AddExperience
        fields="__all__"

class GetAJobForm(forms.ModelForm):
    class Meta:
        model=GetAJob
        fields="__all__"

class CommentsandSuggestionsForm(forms.ModelForm):
    class Meta:
        model=CommentsandSuggestions
        fields="__all__"
