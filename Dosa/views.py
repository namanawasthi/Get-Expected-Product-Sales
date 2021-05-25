from django.shortcuts import render
from . import utilities
from . import forms
from django.contrib import messages

# Create your views here.

def index(request):
    data = utilities.slider_data()
    context = {
        'slider_data':data
        }
    return render(request,'index.html',context)


def contact(request):
    return render(request,'contact.html')
    
def sub_category(request,pk=None):
    data = utilities.get_sub_category_detail(pk)
    context = {
        'sub_category':data
        }
    return render(request,'sub_category.html',context)

def parent_category(request):
    data = utilities.get_parent_category_data()
    context = {
        'parent_category':data
        }

    return render(request,'Parent_category.html',context)

def products(request,pk=None):
    data = utilities.get_products(pk)
    context = {
        'product':data
        }
    return render(request,'products.html',context)

def product_detail(request,pk=None):
    data = utilities.get_product_detail(pk)
    if(request.method == "POST"):
        form = forms.VotingForm(request.POST)
        product_id = request.POST.get("product_id",None)
        voting = request.POST.get("voting",None)
        utilities.done_vote(product_id,voting)
        messages.success(request, 'Thanks For your Kind FeedBack!')
    else:
        form = forms.VotingForm()
    context = {
        'product_detail':data,
        'form':form
        }
    return render(request,'product_detail.html',context)

def email_page(request):
    return render(request,'Email.html')

def about_page(request):
    return render(request,'about.html')







