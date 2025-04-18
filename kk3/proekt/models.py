import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CustomUser(AbstractUser):
    first_name = models.CharField(verbose_name=_('Имя'), max_length=50, blank=False)
    last_name = models.CharField(verbose_name=_('Фамилия'), max_length=50, blank=False)
    middle_name = models.CharField(verbose_name=_('Отчество'), max_length=50, blank=False)
    phone = models.CharField(verbose_name=_('Номер телефона'), max_length=17, blank=False)
    role = models.ForeignKey('Role', verbose_name=_('Роль'), on_delete=models.CASCADE, default=1)
    """ email = models.EmailField(_("Адрес электронной почты"), max_length=254)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 
    Это для авторизации через email"""

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',
        blank=True
    )

    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Role(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Роль'), blank=False)

    def __str__(self):
        return self.name


class Order_table(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Наименование'), blank=False)
    description = models.TextField(verbose_name=_('Описание'), blank=True)
    value = models.DecimalField(verbose_name=_('Значение'), max_digits=10, decimal_places=2)
    image = models.ImageField(verbose_name=_('Изображение'), upload_to='orders/', blank=True, null=True, default='empty.txt')

    def __str__(self):
        return f'{self.name} | {self.value}'


class Status(models.Model):
    code = models.CharField(verbose_name=_('Код статуса'), max_length=50, blank=False)
    name = models.CharField(verbose_name=_('Статус'), max_length=50, blank=False)

    def __str__(self):
        return self.name


class Ticket(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name=_('Пользователь'), on_delete=models.CASCADE, related_name='tickets')
    order = models.ForeignKey(Order_table, verbose_name=_('Товар'), on_delete=models.CASCADE)
    status = models.ForeignKey(Status, verbose_name=_('Статус'), on_delete=models.CASCADE, related_name='tickets_with_status')
    quantity = models.IntegerField(verbose_name=_('Количество'), blank=False)
    detail = models.CharField(verbose_name=_('Дополнительные данные'), max_length=200, blank=False)
    timestamp = models.DateTimeField(_('Дата и время'), auto_now_add=True)

    def __str__(self):
        return f'Заявка {self.id} – {self.order.name} ({self.status.name})'
