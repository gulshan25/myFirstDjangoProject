
from django.urls import path
from . import views

urlpatterns = [
    path('func1/', views.function1),
    path('wc/<str:name>/',views.welcome)
]                                                 # create new file & name urls.py and copied the original project1 folder urls.py