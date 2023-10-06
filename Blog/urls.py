from django.urls import path
from .views import ( PostListView,
	 PostDetailView, 
	 PostCreateView,
	 PostUpdateView,
	 PostDeteleView,
	 UserPostListView,
	 DepartmentPostListView,
	 GroupPostListView,
	 TaskPostListView,
	 Group_TaskPostListView,
	 RegionnamesPostListView,
	 RegionalPostListView,
	 CustomerPostListView,
	 )
from . import views
from expenses import urls

urlpatterns= [
	path('', DepartmentPostListView.as_view(), name='home'),
	path('post/criteria', TaskPostListView.as_view(), name='criteria'),
	path('criteria/<str:criteria>/', Group_TaskPostListView.as_view(), name='criteria-group'),
	path('post/order', PostListView.as_view(), name='post-history'),
	path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
	path('department/<str:department_name>/', GroupPostListView.as_view(), name='group-posts'),
	path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
	path('post/new/', PostCreateView.as_view(), name='post-create'),
	path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
	path('post/<int:pk>/delete', PostDeteleView.as_view(), name='post-delete'),
	path('products_list/', views.products_list, name='products-list'),
	path('region_name/', RegionnamesPostListView.as_view(), name='region-name'),
	path('reginal/<str:region_name>/', RegionalPostListView.as_view(), name='regional'),
	path('customer_list/', CustomerPostListView.as_view(), name='customer-list'),
	path("", views.search_view, name="home"),
]

