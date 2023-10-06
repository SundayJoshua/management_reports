from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField



class Product(models.Model):
	product_name = models.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
		return self.product_name

class Post(models.Model):
	products_ordered = models.CharField(max_length=100)
	evidence = models.TextField()
	date_posted = models.DateTimeField(default=timezone.now)
	date = models.DateField(default=timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(blank=True, upload_to='Posted_img')
	product = models.ManyToManyField('Product')
	approved = models.BooleanField('Approved', default=False)
	day = models.ForeignKey('Day', on_delete=models.SET_NULL, blank=True, null=True)
	department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True)
	criteria = models.ForeignKey('Task', on_delete=models.SET_NULL, blank=True, null=True)
	customer = models.ForeignKey('Customer', on_delete=models.SET_NULL, blank=True, null=True)
	region_name = models.ForeignKey('Region', on_delete=models.SET_NULL, blank=True, null=True)
	contact = models.CharField(max_length=128, blank=True, null=True)

	def __str__(self):
	    return self.title

	def product_name(self):
			return ', '.join([a.product_name for a in self.product.all()])
			product_name.short_description = "Products Orders"


	def get_absolute_url(self):
	    return reverse('post-detail', kwargs={'pk': self.pk})

	@property
	def get_sum(self):
		total = sum([self.post_id])
		return total

	@property
	def get_post_total(self):
		posts = self.Post_set.all()
		total = sum([post.get_total for post in posts])
		return total



class Blogtitle(models.Model):
	"""docstring for blogtitle"""
	title = models.CharField(max_length=100)
	content = models.TextField()

def __str__(self):
    return self.title

    def get_absolute_url(self):
    	return reverse('blogtitle-detail', kwargs={'pk': self.pk})


class Day(models.Model):
	day_of_the_week = models.CharField(max_length=100)

	def __str__(self):
		return self.day_of_the_week


class Department(models.Model):
	department_name = models.CharField(max_length=100)

	def __str__(self):
		return self.department_name


class Task(models.Model):
	criteria = models.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
		return self.criteria

class Response(models.Model):
	response = models.CharField(max_length=256, blank=True, null=True)

	def __str__(self):
		return self.response

class Customer(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Region(models.Model):
	region_name= models.CharField(max_length=100)
	def __str__(self):
		return self.region_name



class Calendar(models.Model):
	memo = models.CharField(max_length=256)
	date = models.DateField('Calendar', default=timezone.now)

	def __str__(self):
		return self.date



