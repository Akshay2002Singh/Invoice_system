from hashlib import new
from http.client import HTTPResponse
from django.shortcuts import render,redirect
from home.models import invoice_details
import json
from .process import html_to_pdf
from django.http import HttpResponse
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    return render(request,"index.html")

def get_invoice_data(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('number')
        address = request.POST.get('address')
        items = request.POST.get('items')
        catagories = request.POST.get('catagories')
        prices = request.POST.get('prices')
        quantities = request.POST.get('quantities')

        temp_details = invoice_details(d_name=name,d_email=email,d_phone=phone,d_address=address,d_items=items,d_catagoried=catagories,d_prices=prices,d_quantities=quantities)
        temp_details.save()

        # temp_contact = contact(name=name,email=email,phone=phone,message=message)
        # temp_contact.save()

        return redirect(all_user_details)
    
def all_user_details(request):
    query = invoice_details.objects.all()
    context={"user_data" : query}
    # print(context)
    return render(request,'all_user_details.html',context=context)


def generate_invoice(request,id):
    # print(id)
    query = invoice_details.objects.get(id=id)

    items = json.loads(query.d_items)
    catagories = json.loads(query.d_catagoried)
    prices = json.loads(query.d_prices)
    quantity = json.loads(query.d_quantities)

    new_context={
        "id" : query.id,
        "d_name" : query.d_name,
        "d_email" : query.d_email,
        "d_phone" : query.d_phone,
        "d_address" : query.d_address,
    }
    temp = []
    total = 0
    for i in range(len(items)):
        temp.append({"item":items[i],"catagory":catagories[i],"price":prices[i],"quantity":quantity[i],"total":prices[i]*quantity[i]})
        total += prices[i]*quantity[i]
    
    new_context["data"] = temp
    new_context["g_total"] = total

    # print(new_context)


    return render(request,"invoice.html",context=new_context)


def generate_pdf(request,id):
    # print(id)
    query = invoice_details.objects.get(id=id)

    items = json.loads(query.d_items)
    catagories = json.loads(query.d_catagoried)
    prices = json.loads(query.d_prices)
    quantity = json.loads(query.d_quantities)

    new_context={
        "id" : query.id,
        "d_name" : query.d_name,
        "d_email" : query.d_email,
        "d_phone" : query.d_phone,
        "d_address" : query.d_address,
    }
    temp = []
    total = 0
    for i in range(len(items)):
        temp.append({"item":items[i],"catagory":catagories[i],"price":prices[i],"quantity":quantity[i],"total":prices[i]*quantity[i]})
        total += prices[i]*quantity[i]
    
    new_context["data"] = temp
    new_context["g_total"] = total

    # print(new_context)

    open('templates/temp.html', "w").write(render_to_string('print_invoice.html',new_context ))
    pdf = html_to_pdf('temp.html')
    return HttpResponse(pdf, content_type='application/pdf')

    # return render(request,"invoice.html",context=new_context)