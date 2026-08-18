from django.shortcuts import render,redirect,get_object_or_404
from . models import  Product
from . forms import  ProductForm

# Fetching all products
def product_list(request):
    products=Product.objects.all()
    return render (request,'product_list.html',context={'products':products})


def product_create(request):
    form = ProductForm(request.POST or None)
    if request.method =='POST' and form.is_valid():
        form.save()
        return redirect('product_list')
    return render(request,'product_create.html',context={'form':form})

def product_update(request,id):
    product=get_object_or_404(Product,id=id)
    form = ProductForm(request.POST or None , instance=product)
    if form.is_valid():
        form.save()
        return redirect('product_list')
    return render (request,'product_update.html',context={'form':form})


def product_delete(request,id):
    product = get_object_or_404(Product,id=id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request,'product_delete.html',context={'product':product})