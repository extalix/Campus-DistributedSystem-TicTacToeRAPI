from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='userHome'),
    path('', views.index, name='userHome'),
    path('login', views.login_request, name='loginAccount'),
    path('signup', views.sign_up, name='createAccount'),
    path('logout', views.logout_request, name='logoutAccount'),
]
