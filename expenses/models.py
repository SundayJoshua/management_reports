from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField

# Create your models here.

class Expense(models.Model):
	expense_name = models.CharField(max_length=256)
	amount = models.DecimalField(max_digits=10, decimal_places=2)

	def __str__(self):
		return self.expense_name