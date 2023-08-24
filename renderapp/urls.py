from django.urls import path
from renderapp import views
urlpatterns=[
    path('',views.home,name='home'),
]