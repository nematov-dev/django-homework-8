from django.shortcuts import render,redirect
from django.contrib import messages

from . import forms

def main_page_view(request):
    return render(request,'index.html')

def home_page_view(request):

    if request.path == '/en/home/' or '/uz/home/':
        header_type = 'home_header'
    else:
        header_type = 'default_header'
    
    return render(request, 'pages/home.html', {'header_type': header_type})

def blog_page_view(request):
    return render(request,'blogs/blog.html')

def blog_detail_page_view(request):
    return render(request,'blogs/blog_detail.html')

def product_page_view(request):
    return render(request,'products/product.html')

def product_detail_page_view(request):
    return render(request,'products/product_detail.html')

def about_page_view(request):
    return render(request,'pages/about.html')

def contact_page_view(request):

    if request.method == "POST":
        
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your message save database')
            return redirect('pages:contact')

        else:
            messages.error(request,'Error')
            return redirect('pages:contact')

    else:
        return render(request,'pages/contact.html')