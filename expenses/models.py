from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food','Food & Dining'),
        ('Transport','Transport'),
        ('Bills','Bills & Utilities'),
        ('Entertainment', 'Entertainment'),
        ('Other','Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Food')
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"