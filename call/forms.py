from django import forms
from django.core import validators
from .models import *
GEEKS_CHOICES =(
    ( "Lahore","Lahore",),
    ("Karachi", "Karachi"),
    ("Fasilabad", "Fasilabad"),
    ("Multan", "Multan"),
    ("Peshawar", "Peshawar"),
    ("Islamabad", "Islamabad")
    )
class patientloginform(forms.ModelForm):

    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':"(12345678)", 'id':"text-da93", 'name':"text", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle",'required':'required'}))
    City=forms.ChoiceField(choices=GEEKS_CHOICES,widget= forms.Select(attrs={'id':"select-5620", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}))
    class Meta:
        widgets = {
        'name':forms.TextInput(attrs={'id':'name-f2a8','class': 'u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle', 'placeholder': 'Enter your Name', 'required': 'required'}),
        'Email':forms.TextInput(attrs={'placeholder':"Enter a valid email address" ,'id':"email-f2a8" ,'name':"email", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'DOB':forms.TextInput(attrs={ 'placeholder':"YYYY/MM/DD/", 'id':"date-4441", 'name':"date", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'phone':forms.TextInput(attrs={'type':"tel", 'pattern':"+92\d{10}", 'placeholder':"Enter your phone (e.g. +923034498139)", 'id':"phone-447e", 'name':"phone", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'password':forms.PasswordInput(attrs={ 'placeholder':"(12345678)" ,'id':"text-6fae", 'name':"Password" , 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'cnic':forms.TextInput(attrs={'placeholder':"35202-1299-155-1", 'id':"text-5d78", 'name':"cnic", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required':"required"}),
        'longitude':forms.TextInput(attrs={'type':"number",'onclick':"getLocation()", 'step':"any",  'id':"text-d4f2" , 'name':"longitude", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required':"required"}),
        'lattitude':forms.TextInput(attrs={'type':"number", 'onclick':"getLocation()" ,'step':"any",  'id':"text-0f6e", 'name':"latitude", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle",'required':"required"}),
        
        }
        model = patientlogin
        fields = "__all__"
        def clean(self):
            cleaned_data = super(patientloginform, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError(
                "password and confirm_password does not match")
class registrationalter(forms.Form):
  #  email=forms.EmailField()
    email = forms.CharField(widget=forms.TextInput(attrs={'type':"email",'placeholder':"Enter a valid email address", 'id':"email-319a", 'name':"email" , 'class':"u-border-2 u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle",'required':'required'}))
    password = forms.CharField(widget = forms.TextInput(attrs={'type':"password",'placeholder':"12345678", 'id':"text-c0b5", 'name':"Password" , 'class':"u-border-2 u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle", 'required':'required'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={'placeholder':"12345678", 'id':"text-8a43", 'name':"text-1", 'class':"u-border-2 u-border-no-left u-border-no-right u-border-no-top u-border-white u-input u-input-rectangle",'required':'required'}))
class doctorloginform(forms.ModelForm):

    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={ 'placeholder':"12345678", 'id':"text-5d07", 'name':"text", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle",'required':'required'}))
    City=forms.ChoiceField(choices=GEEKS_CHOICES,widget= forms.Select(attrs={'id':"select-5449", 'name':" Select", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}))
    
    class Meta:
        widgets = {
        'name':forms.TextInput(attrs={'type':"text", 'placeholder':"Enter your Name", 'id':"name-f2a8", 'name':"name", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'Email':forms.TextInput(attrs={'placeholder':"Enter a valid email address", 'id':"email-f2a8", 'name':"email", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'DOB':forms.TextInput(attrs={  'placeholder':"YYYY/MM/DD", 'id':"date-4441", 'name':"date", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'phone':forms.TextInput(attrs={'type':"tel", 'pattern':"+92\d{10}", 'placeholder':"Enter your phone (e.g. +923034498139)", 'id':"phone-447e", 'name':"phone", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'password':forms.PasswordInput(attrs={ 'type':"password", 'placeholder':"12345678", 'id':"text-ef55", 'name':"password", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required': 'required'}),
        'cnic':forms.PasswordInput(attrs={'type':"text", 'placeholder':"35202-1299155-1" , 'id':"text-4279", 'name':"cnic", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle"}),
        'longitude':forms.TextInput(attrs={'type':"number", 'step':"any", 'onClick':"getLocation()",  'id':"text-f824", 'name':"longitude", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required':"required"}),
        'lattitude':forms.TextInput(attrs={'type':"number",'step':"any", 'onclick':"getLocation()",  'id':"text-8220", 'name':"latitude", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required':"required"}),
        'pmdc':forms.TextInput(attrs={'type':"text", 'placeholder':"352021", 'id':"text-7824", 'name':"text-1", 'class':"u-border-2 u-border-grey-75 u-border-no-left u-border-no-right u-border-no-top u-input u-input-rectangle", 'required':"required"})
        }
        model = doctorlogin
        fields = "__all__"
       
        def clean(self):
            cleaned_data = super(doctorloginform, self).clean()
            password = cleaned_data.get("password")
            confirm_password = cleaned_data.get("confirm_password")

            if password != confirm_password:
                raise forms.ValidationError(
                "password and confirm_password does not match")
class doctorregistrationalter(forms.Form):
  #  email=forms.EmailField()
    email = forms.CharField(widget=forms.TextInput(attrs={'type':"email", 'placeholder':"Enter a valid email address", 'id':"email-daf4", 'name':"email", 'class':"u-border-2 u-border-white u-input u-input-rectangle u-radius-12 u-white",'required':'required'}))
    password = forms.CharField(widget = forms.TextInput(attrs={ 'type':"password",'placeholder':"12345678", 'id':"text-9bcd", 'name':"text", 'class':"u-border-2 u-border-white u-input u-input-rectangle u-radius-12 u-white", 'required':'required'}))
    confirm_password = forms.CharField(widget = forms.PasswordInput(attrs={ 'placeholder':"12345678", 'id':"text-ea38", 'name':"text-1", 'class':"u-border-2 u-border-white u-input u-input-rectangle u-radius-12 u-white",'required':'required'}))
class patientprofile(forms.ModelForm):
    class Meta:
        model =patientlogin
        fields = ['image'] 
   
class doctorprofile(forms.ModelForm):
    class Meta:
        model =doctorlogin
        fields = ['image'] 
      