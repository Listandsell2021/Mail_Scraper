from django.urls import path
from scrap import views

urlpatterns = [
    # path('', views.form_request,name='form_request'),   
     path('', views.hello_view, name='hello'),
]