from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.

from .models import Role, Status, Order_table, Ticket, CustomUser
from .forms import RegistrationForm, TicketForm

def mainpage(request):
    return render(request, 'base.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            default_role = get_object_or_404(Role, name='Пользователь')
            user.role = default_role
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('user_tickets')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_tickets')
        else:
            messages.error(request, ' Неправильный логин или пароль')
    else:
        form = AuthenticationForm()
        
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def user_tickets(request):
    tickets = Ticket.objects.filter(user=request.user)
    return render(request, 'user_tickets.html', {'tickets': tickets})
    
@login_required
def create_ticket(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            default_status = get_object_or_404(Status, code='new')
            ticket.status = default_status
            ticket.save()
            return redirect('user_tickets')
    else:
        form = TicketForm()
        
    entities = Order_table.objects.all()
    return render(request, 'create_ticket.html', {'form': form, 'entities': entities})