from django.urls import path
from .views import HomeView, AboutView, ServiceView, ContactView, LoginView, SignupView

urlpatterns = [
    path('api/home/', HomeView.as_view(), name='home'),
    path('api/about/', AboutView.as_view(), name='about'),
    path('api/service/', ServiceView.as_view(), name='service'),
    path('api/contact/', ContactView.as_view(), name='contact'),
    path('api/login/', LoginView.as_view(), name='login'),
    path('api/signup/', SignupView.as_view(), name='signup'),
]

