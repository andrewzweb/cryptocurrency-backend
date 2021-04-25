from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token

app_name = 'account'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login_account, name='login'),
    path('logout/', views.logout_account, name='logout'),
    path('token-auth/', obtain_jwt_token, name='token')
 ]
