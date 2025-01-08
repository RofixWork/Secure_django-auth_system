from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from . import views as api_views

urlpatterns = [
    path("user/token/", api_views.MyTokenObtainPairAPIView.as_view()),
    path("user/token/refresh/", TokenRefreshView.as_view()),
    path("user/sign-up/", api_views.UserRegisterAPIView.as_view()),
    path(
        "user/dashboard/", api_views.DashboardView.as_view()
    ),  # replace with your own view name and method
]
