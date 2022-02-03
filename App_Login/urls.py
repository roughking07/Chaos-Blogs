from django.urls import path
from django.contrib.auth import views as auth_views  

from . import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sing_up, name='signup'),
    path('signin/', views.login_page, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-profile/', views.user_change, name='user_change'),
    path('password/', views.pass_change, name='pass_change'),
    path('change-profile-image/', views.add_pro_pic, name='add_pro_pic'),
    path('change-picture/', views.change_pro_pic, name='change_pro_pic'),
    
    #reset-password
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name="password_reset_complete"),   
]
