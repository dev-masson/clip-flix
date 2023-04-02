from django.urls import path, reverse_lazy
from .views import HomePage, HomeClips, DetailsClips, SearchClip, EditProfile, Register
from django.contrib.auth import views as auth_view


app_name = 'clip'

urlpatterns = [
    path('', HomePage.as_view(), name='homepage'),
    path('clips/', HomeClips.as_view(), name='homeclips'),
    path('clips/<int:pk>/', DetailsClips.as_view(), name='detailsclips'),
    path('search/', SearchClip.as_view(), name='search'),
    path('login/', auth_view.LoginView.as_view(template_name='login.html',
                                               success_url=reverse_lazy('clip:homeclips')), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/',  Register.as_view(), name='register'),
    path('editprofile/<int:pk>', EditProfile.as_view(), name='editprofile'),
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='editprofile.html',
                                                                 success_url=reverse_lazy('clip:homeclips') ), name='password_change'),
]  
