from django.db import models
import datetime

# Create your models here.

class User(models.Model):
    login = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return f"Пользователь ({self.login})"

class Category(models.Model):
    title = models.CharField(max_length=100)
    def __str__(self):
        return f"Категория ({self.title})"

class Transaction(models.Model):
    title = models.CharField(max_length=100)
    total = models.FloatField()
    type = models.BooleanField(verbose_name="Доход")
    date = models.DateField(default=datetime.datetime.now())
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    def __str__(self):
        return f"Операция ({self.title})"
    
