from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('profile/', views.ProfileDetailView.as_view(), name='profile'),
    path('profile/edit/', views.ProfileUpdateView.as_view(), name='profile_edit'),
]