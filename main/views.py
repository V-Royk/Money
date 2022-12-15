from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import SignUpForm, SignInForm, TransactionForm
from .models import User, Transaction, Category
import json



# Create your views here.
def signup(request):
    form = SignUpForm()
    return render(request, "signup.html", {"form" : form})



def signin(request):
    form = SignInForm()
    return render(request, "signin.html", {"form" : form})


def main(request):
    transactions = reversed(Transaction.objects.all())
    categories = Category.objects.all() 
    users = User.objects.filter(id=request.session.get("user_id"))
    if len(users) > 0:
        user = users[0]
    else:
        return redirect("signin")
    form = TransactionForm()
    return render(request, "main.html", {"transactions" : transactions, 'categories' : categories, "form" : form, "user" : user})


def registrate(request):
    if request.method == 'POST':
        data = request.POST
        login = data.get("login", False)
        password = data.get("password", False)
        re_password = data.get("re_password", False)
        if password == re_password and User.objects.filter(login=login).count() == 0:
            User.objects.create(login=login, password=password)
            return render(request, "main.html")
        else:
            form = SignUpForm()
            return render(request, "signup.html", {"form" : form, "errors" : ["Неверно введены данные"]})

def auth(request):
    if request.method == 'POST':
        data = request.POST
        login = data.get("login", False)
        password = data.get("password", False)
        if User.objects.filter(login=login, password=password).count() != 0:
            request.session["user_id"] = User.objects.get(login=login, password=password).id
            return redirect("main")
        else:
            form = SignInForm()
            return render(request, "signin.html", {"form" : form, "errors" : ["Неверно введены данные"]})


def addTransaction(request):
    if request.method == 'POST':
        transaction = Transaction()
        transaction.title = request.POST.get("title")
        transaction.total = request.POST.get("total")
        transaction.type = True if request.POST.get("type") else False
        transaction.category = Category.objects.get(id=request.POST.get("category"))
        transaction.user = User.objects.get(id=request.session.get("id", 1))
        transaction.date = request.POST.get('date')
        transaction.save()
        return redirect("main")

def spendings(request):
    transactions = [
        {
            "id" : transaction.id,
            "title" : transaction.title,
            "total" : transaction.total,
            "category" : transaction.category.title
        }
        for transaction in
        Transaction.objects.filter(user=User.objects.get(id=request.session.get("id", 1)), type=0)
    ]
    return JsonResponse(json.dumps(transactions), safe=False)



def income(request):
    transactions = [
        {
            "id" : transaction.id,
            "title" : transaction.title,
            "total" : transaction.total,
            "category" : transaction.category.title
        }
        for transaction in
        Transaction.objects.filter(user=User.objects.get(id=request.session.get("id", 1)), type=1)
    ]
    return JsonResponse(json.dumps(transactions), safe=False)
    

def delete(request, id):
    try:
        transactions = Transaction.objects.get(id=id)
        transactions.delete()
        return redirect("main")
    except Transaction.DoesNotExist:
        return redirect("main")






