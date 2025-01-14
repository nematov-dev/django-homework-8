from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('contact/',views.contact_page_view,name='contact'),
    path('about/',views.about_page_view,name='about'),
    path('product/',views.product_page_view,name='product'),
    path('product/product-detail',views.product_detail_page_view,name='product_detail'),
    path('blog/',views.blog_page_view,name='blog'),
    path('blog/blog-detail/',views.blog_detail_page_view,name='blog_detail'),
    path('home/',views.home_page_view,name='home'),
    path('',views.main_page_view,name='main')
]