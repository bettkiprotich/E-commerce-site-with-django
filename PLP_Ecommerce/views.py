from django.shortcuts import render, get_list_or_404
from.models import Product, Customer

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    context={
        'products':products
    }
    return render(request,'Ecommerce/product_list.html',context)

def product_detail(request,pk):
    product= get_objects_or_404(Product,pk=pk)
    context={
        'product':product
    }
    return render(request,'Ecommerce/product_detail.html',context)

def customer_list(request):
    customer= Customer.objects.all()
    context={
        'customer':customer
    }
    return render(request,'Ecommerce/customer_list.html',context)

def customer_detail(request):
    customer= get_list_or_404(customer,pk=pk)
    context={
        'customer':customer
    }
    return render(request,'Ecommerce/customer_list.html',context)
    