from django.urls import path
from Airline import views


urlpatterns=[
    path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('blog_single',views.blog_single,name='blog_single'),
    path('index',views.index,name='index'),
    path('contact',views.contact,name='contact'),
    path('portfolio',views.portfolio,name='portfolio'),
]

