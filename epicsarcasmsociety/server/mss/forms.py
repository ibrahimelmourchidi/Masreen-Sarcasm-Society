from django import forms
from django.contrib.auth import authenticate ,login
from django.contrib.auth.models import User
from .models import Post 
from django.shortcuts import render , redirect , get_object_or_404,HttpResponseRedirect

class addComic(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','image']
	
class addvedio(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content','vedio_url']


class confirm_form(forms.ModelForm):
	confirmation_code = forms.CharField(label = "", widget = forms.TextInput(attrs = {
					"placeholder":"6-digits confirmation code"
				}
			) )
	class Meta:
		model = User
		fields = ["confirmation_code"]

class edit_profile(forms.ModelForm):
	class Meta:
		model = User
		fields = ["p_image"]


class LoginForm(forms.Form):
	username = forms.CharField(label = "" ,widget = forms.TextInput(attrs = {
					"placeholder":"User Name or Email"
				}
			))
	password = forms.CharField(label = "" , widget = forms.PasswordInput(attrs = {
					"placeholder":"Password"
				}
			))
	def clean_username(self):
		getusername = self.cleaned_data.get("username")
		if "@" in getusername :
			qs = User.objects.filter(email =getusername)
			if not qs:
				raise forms.ValidationError("Email is not registered , Please check the email.")
			else:
				username = qs[0].username
		else:
			username = getusername
		return username
	def clean_password(self):
		password = self.cleaned_data.get("password")
		return password




class UserRegister(forms.ModelForm):
	password = forms.CharField(widget = forms.PasswordInput)
	password2 = forms.CharField(widget = forms.PasswordInput)
	class Meta:
		model = User
		fields = ['username','email','password','password2']

	def clean_username(self):
		username = self.cleaned_data.get("username")
		if "@" in username:
			raise forms.ValidationError("UserName cannot contain @")
		return username
	def clean_password(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		return password
	def clean_password2(self):
		password = self.cleaned_data.get("password")
		password2 = self.cleaned_data.get("password2")
		if not password == password2:
			print(password) 
			print(password2)
			raise forms.ValidationError("Passwords donot match")
		return password2