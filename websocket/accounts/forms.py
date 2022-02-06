from attr import fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms






class SignUpForm(forms.ModelForm):
    
    class Meta:
        model  = User 
        fields = ['first_name','last_name','username','email','password']
        
        
    
        def create(self, validated_data):
            user = User(**validated_data)
            user.set_password(validated_data['password'])
            user.save()
            return user
    
    