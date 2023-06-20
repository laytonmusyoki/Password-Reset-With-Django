from django.urls import path
from django.contrib.auth import views as auth_views
from .views import home,register,loginpage,Logout

urlpatterns=[
    path('',home,name='home'),
    path('register/',register,name='register'),
    path('loginpage/',loginpage,name='loginpage'),
    path('Logout/',Logout,name='Logout'),


    path('reset_password/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), 
         name="reset_password"),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_send.html'), 
         name="password_reset_done"),

    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), 
         name="password_reset_confirm"),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), 
         name="password_reset_complete")
]