from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.signup_view

def signup_view(request):
	form = UserCreationForm
	return render(request,'signup.html',{'form':form})