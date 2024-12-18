from django.shortcuts import render
from django.http import HttpResponse
# from scrap.models import Websites_Model

# def form_request(request):
#     # website_name = Websites_Model.objects.all()
#     return render(request, 'form.html')

def hello_view(request):
    return HttpResponse("Hello")
