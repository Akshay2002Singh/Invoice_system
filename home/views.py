from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def get_invoice_data(request):
    print("got")

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        address = request.POST.get('address')
        items = request.POST.get('items')
        catagories = request.POST.get('catagories')
        prices = request.POST.get('prices')
        quantities = request.POST.get('quantities')

        # temp_contact = contact(name=name,email=email,phone=phone,message=message)
        # temp_contact.save()

        return render(request,'next.html')