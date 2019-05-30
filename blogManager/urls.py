from django.urls import path
from . import views

app_name = 'blogManager'
urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('<int:pk>/update', views.PostUpdateView.as_view(), name='update'),
    path('<int:pk>/delete', views.PostDeleteView.as_view(), name='delete'),
    path('create/', views.PostCreateView.as_view(), name='create'),
]