from django import forms
from .models import Category
import datetime

class SignUpForm(forms.Form):
    login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Логин", 'class':"inp"}), label="")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"placeholder" : "Пароль", 'class':"inp"}), label="")
    re_password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"placeholder" : "Повторите пароль", 'class':"inp"}), label="")



class SignInForm(forms.Form):
    login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Логин", 'class':"inp"}), label="")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"placeholder" : "Пароль", 'class':"inp"}), label="")
  
class TransactionForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Название"}), label="")
    total = forms.FloatField(widget=forms.NumberInput(attrs={"placeholder" : "Сумма", "min" : 1}), label="")
    type = forms.BooleanField(label="Доход", required=False)
    category = forms.ChoiceField(choices=((category.id, category.title) for category in Category.objects.all()), label="")
    date = forms.DateField(widget=forms.DateInput(attrs={"type" : "date", "value" : datetime.date.today()}), label="")