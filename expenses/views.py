from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from . models import Expense
# Create your views here.

class PostCreateView(CreateView):
	model = Expense
	fields = ['expense_name', 'amount']
	success_url = '/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		messages.add_message(self.request, messages.INFO, 'Your report has been submitted!')
		return super().form_valid(form)


class PostListView(ListView):
	paginate_by = 20
	model = Expense
	template_name = 'expenses/expense_list.html'
	context_object_name = 'expenses'
