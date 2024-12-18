from django.shortcuts import render
from scrap.models import Websites_Model

def form_request(request):
    website_name = Websites_Model.objects.all()
    return render(request, 'form.html',{'website_name':website_name})
