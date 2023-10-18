from django.urls import path
from . import views
urlpatterns = [

path('',views.signup),
path('validation/',views.uniq_check,name='uniq_check'),
path('success/',views.success,name='success')


]