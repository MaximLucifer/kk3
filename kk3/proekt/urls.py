from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage, name='mainpage'),
    path('register/', views.register ,name='register'),
    path('login/', views.login_view ,name='login'),
    path('logout/', views.logout_view ,name='logout'),
    path('tickets/', views.user_tickets ,name='user_tickets'),
    path('tickets/create', views.create_ticket ,name='create_ticket'),
]
