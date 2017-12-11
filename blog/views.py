from django.http import HttpResponse
from django.shortcuts import render

from .models import Article


def home(request):
	return render(request,'home.html')

def about(request):
	return render(request,'about.html')


def article(request):
	articles = Article.objects.all().order_by('date')
	return render(request,'article.html',{ 'articles':articles })

def article_detail(request,slug):
	# return HttpResponse(slug)
	article = Article.objects.get(slug=slug)
	return render(request,'articled.html',{'article':article})
