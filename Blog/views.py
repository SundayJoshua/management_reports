from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.http import HttpResponseRedirect
from .forms import UploadFileForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import CalendarPlanForm
from django.contrib.auth.decorators import permission_required
from django.db.models import Q, Sum
from django.core.mail import send_mail


def img(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			#file is saved
			form.save()
			return HttpResponseRedirect('/static/img/')
		else:
			form = UploadFileForm()
			return render(request, 'Blog/home.html', {'form': form})


class PostListView(ListView):
	paginate_by = 20
	model = Post
	template_name = 'Blog/post_history.html'  #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']


class DepartmentPostListView(ListView):
	paginate_by = 20
	model = Department
	template_name = 'Blog/home.html'  #<app>/<model>_<viewtype>.html
	context_object_name = 'departments'
	queryset = Post.objects.all()
	ordering = ['-department_name']
	
	def get_queryset(self):
		q = self.request.GET.get('q')
		if q:
			object_list = self.model.objects.filter(
				Q(department_name__icontains=q)
				)
		else:
			try:
				''
			except Exception as e:
				raise
			else:
				pass
			object_list = self.model.objects.all()
		return object_list


	def get_context_data(self, **kwargs):
		context =super().get_context_data(**kwargs)
		context["post_count"] = Post.objects.all().count()
		context["user_count"] = User.objects.all().count()
		context["customer_count"] = Customer.objects.all().count()
		context["product_count"] = Product.objects.all().count()
		return context


class TaskPostListView(ListView):
	paginate_by = 20
	model = Task
	template_name = 'Blog/criteria.html'  #<app>/<model>_<viewtype>.html
	context_object_name = 'tasks'
	queryset = Post.objects.all()

	def get_queryset(self):
		q = self.request.GET.get('q')
		if q:
			object_list = self.model.objects.filter(
				Q(criteria__icontains=q)
				)
		else:
			try:
				''
			except Exception as e:
				raise
			else:
				pass
			object_list = self.model.objects.all()
		return object_list


class RegionnamesPostListView(ListView):
	paginate_by = 20
	model = Region
	template_name = 'Blog/region.html'  #<app>/<model>_<viewtype>.html
	context_object_name = 'regions'
	queryset = Post.objects.all()

	def get_queryset(self):
		q = self.request.GET.get('q')
		if q:
			object_list = self.model.objects.filter(
				Q(region_name__icontains=q)
				)
		else:
			try:
				''
			except Exception as e:
				raise
			else:
				pass
			object_list = self.model.objects.all()
		return object_list


class GroupPostListView(ListView):
	paginate_by = 20
	model = Post
	template_name = 'Blog/group_posts.html'  #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] 

	def get_queryset(self):
		department_name = get_object_or_404(Department, department_name=self.kwargs.get('department_name'))
		return Post.objects.filter(department=department_name).order_by('-date_posted')

class Group_TaskPostListView(ListView):
	paginate_by = 20
	model = Post
	template_name = 'Blog/criteria_group.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	
	def get_queryset(self):
		criteria = get_object_or_404(Task, criteria=self.kwargs.get('criteria'))
		return Post.objects.filter(criteria=criteria).order_by('-date_posted')	

class RegionalPostListView(ListView):
	paginate_by = 20
	model = Post
	template_name = 'Blog/regional_reports.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	
	def get_queryset(self):
		region_name = get_object_or_404(Region, region_name=self.kwargs.get('region_name'))
		return Post.objects.filter(region_name=region_name).order_by('-date_posted')

class CustomerPostListView(ListView):
	paginate_by = 20
	model = Customer
	template_name = 'Blog/customer_list.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'customers'

	
	
class UserPostListView(ListView):
	model = Post
	template_name = 'Blog/user_posts.html'  #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted'] 

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['department', 'date', 'product', 'criteria', 'customer', 'contact', 'region_name', 'products_ordered', 'evidence']
	success_url = '/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		messages.add_message(self.request, messages.INFO, 'Your report has been submitted!')
		return super().form_valid(form)

		"""If the form is valid, redirect to the supplied URL."""
		"""return HttpResponseRedirect(self.get_success_url('home')) """

		
        
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['department', 'products_ordered', 'date', 'evidence']
	success_url = '/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)  

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False      


class PostDeteleView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False



def products_list(request):
	products = Product.objects.all()
	paginator = Paginator(products, 20)
	page_number = request.GET.get('page')
	products = paginator.get_page(page_number)
	context = {
		'products': products
	}
	return render(request, 'Blog/products_list.html', context)


def admin_approval(request):
	post_list = Post.objects.all()
	if request.user.is_superuser:
		if request.method == "POST":
			id_list = request.POST.getlist('boxes')
			print(id_list)

			approved_list.update(approved=False)

			for x in id_list:
				Post.objects.filter(pk=int(x)).update(approved=true)

			messages.success(request, ('Has been approved'))
			return redirect('/')
	else:
		return render(request, 'Blog/group_posts.html', {'post_list': post_list})



def search_view(request):
	post_count = Post.objects.all().count()
	context = {'post_count': post_count}

	return render(request, "Blog/home.html", context)


