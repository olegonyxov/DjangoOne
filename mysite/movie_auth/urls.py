from django.urls import path

from . import views

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('log_out/', views.log_out, name='log_out'),
    path('api/sign_up/', views.AuthSignUp.as_view(), name='api_sign_up'),
    path('api/sign_in/', views.AuthSignIn.as_view(), name='api_sign_in'),
    path('api/logout/', views.Logout.as_view(), name='api_Logout')

]
