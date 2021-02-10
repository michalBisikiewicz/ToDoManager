from django.urls import path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signupuser/', views.signupuser, name='signupuser'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
