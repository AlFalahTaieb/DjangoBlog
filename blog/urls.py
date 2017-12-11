from django.conf.urls import url



from . import views
app_name='blog'

urlpatterns = [
    url(r'^about/$',views.about),
    url(r'^article/',views.article, name='list'),
    url(r'^$',views.home),
    url(r'^(?P<slug>[\w-]+)/$',views.article_detail,name="detail")
]
