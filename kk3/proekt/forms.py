from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from .models import Role, Status, Order_table, CustomUser, Ticket

class RegistrationForm(UserCreationForm):
    username = forms.CharField(label=_('Логин'), max_length=50, required=True)
    first_name = forms.CharField(label=_('Имя'), max_length=50, required=True)
    last_name = forms.CharField(label=_('Фамилия'), max_length=50, required=True)
    middle_name = forms.CharField(label=_('Отчество'), max_length=50, required=True)
    phone = forms.CharField(label=_('Номер телефона'), max_length=50, required=True)
    email = forms.CharField(label=_('Адрес электронной почты'), required=True)
    
    """ email = forms.EmailField(required=True)  
    Это для авторизации через email"""
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name', 'middle_name', 'phone']
        """ fields = ['email', 'password1', 'password2'] """
        labels = {
            'username': _('Введите логин'),
            'email': _('Введите Email'),
            'password1': _('Введите пароль'),
            'password2': _('Подтвердите пароль')
        }
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.middle_name = self.cleaned_data['middle_name']
        user.phone = self.cleaned_data['phone']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
class TicketForm(forms.ModelForm):
    
    class Meta:
        model = Ticket
        fields = ['order', 'quantity', 'detail']
        labels = {
            'order': _('Выберите'),
            'quantity': _('Количество'),
            'detail': _('Дополнительные данные'),
        }
        widgets = {
            'order': forms.Select(),
        }