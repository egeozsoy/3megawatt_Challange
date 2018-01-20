from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$', views.index , name='index'),
    url(r'^sites/$' , views.index , name = 'index'),
    url(r'^sites/' , views.site , name = 'site'),
    url(r'^summary-average/', views.average, name ='summary'),
    url(r'^summary/', views.summary, name ='summary')

]
