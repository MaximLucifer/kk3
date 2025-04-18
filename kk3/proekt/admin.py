from django.contrib import admin
from .models import CustomUser, Role, Order_table, Status, Ticket
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'first_name', 'last_name', 'middle_name', 'role', 'phone')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Личная информация'), {'fields': ('first_name', 'last_name', 'middle_name', 'phone', 'email')}),
        (_('Права доступа'), {'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
        (_('Даты'), {'fields': ('last_login','date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'middle-name', 'phone', 'email', 'role',)
        })
    )
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    
@admin.register(Order_table)
class Order_tableAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'value')
    search_fields = ['name']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['code', 'name']
    search_fields = ['name']
    
@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id','user','order','quantity','status','timestamp']
    list_filter = ('status'),
    search_fields = ('user__username','order__name'),
    autocomplete_fields = ('user','order')
    readonly_fields = ['timestamp']


