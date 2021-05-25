from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='home'),
    path('sub_category/<int:pk>',views.sub_category,name='sub_category'),
    path('parent_category/',views.parent_category,name='parent_category'),
    path('product_detail/<int:pk>/',views.product_detail,name='product_detail'),
    path('product/<int:pk>/',views.products,name='product'),
    path('Email/',views.email_page,name='Email'),
    path('about/',views.about_page,name='about'),
    path('contact/',views.contact,name='contact'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

