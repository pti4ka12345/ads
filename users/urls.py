from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework import routers

from users import views
from users.views import LokationViewSet

router = routers.SimpleRouter()
router.register(r'location', LokationViewSet)

urlpatterns = [
    path('user/', views.UserListView.as_view()),
    path('user/<int:pk>', views.UserDetailView.as_view()),
    path('user/create/', views.UserCreateView.as_view()),
    path('user/<int:pk>/update/', views.UserUpdateView.as_view()),
    path('user/<int:pk>/delete/', views.UserDeleteView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    ]

urlpatterns += router.urls
