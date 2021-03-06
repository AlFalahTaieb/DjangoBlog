from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# Create your views here.signup_view
from django.contrib.auth import login,logout

def signup_view(request):
	if request.method =='POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('blog:list')
	else:
		form = UserCreationForm()
	return render(request,'signup.html',{'form':form})      

def login_view(request):
	if request.method =='POST':
		form= AuthenticationForm(data=request.POST)
		if form.is_valid():
			return redirect('blog:list')
	else:
		form = AuthenticationForm()
		return render(request,'login.html',{'form':form})

def logout_view(request):
	if request=='POST':
		logout(request)
		return redirect('blog:list')
