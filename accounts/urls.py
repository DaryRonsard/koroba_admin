# urls.py

from django.urls import path

from accounts.account_views.login_view import LoginView
from accounts.account_views.register_view import SignupView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
]
