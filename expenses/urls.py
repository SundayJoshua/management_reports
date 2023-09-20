from django.urls import path
from .views import ( PostListView, 
	 PostCreateView,
	 )
from . import views


urlpatterns =[
	path('expense_form/', PostCreateView.as_view(template_name='expenses/expense_list.html'), name='create-expense'),
	path('expense_list/', PostListView.as_view(template_name='expenses/expense_list.html'), name='expense-list'),
]