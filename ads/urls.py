from django.contrib import admin
from django.urls import path, include

from ads import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api_auth/', include('rest_framework.urls')),
    path('index/', views.index),
    path('cat/', views.CategoryView.as_view()),
    path('cat/<int:pk>/', views.CategoryDetailView.as_view()),
    path('cat/create/', views.CategoryCreateView.as_view()),
    path('cat/<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('cat/<int:pk>/delete/', views.CategoryDeleteView.as_view()),
    path('ad/', views.AdView.as_view()),
    path('ad/<int:pk>/', views.AdDetailView.as_view()),
    path('ad/create/', views.AdCreateView.as_view()),
    path('ad/<int:pk>/update/', views.AdUpdateView.as_view()),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view()),
    path('ad/<int:pk>/upload_image/', views.AdUploadImageView.as_view()),
    path('selection/', views.SelectionListView.as_view()),
    path('selection/<int:pk>/', views.SelectionUpdateView.as_view()),
    path('selection/create/', views.SelectionCreateView.as_view()),
    path('selection/<int:pk>/update/', views.SelectionUpdateView.as_view()),
    path('user/', include("users.urls")),
]


