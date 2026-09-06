from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('book/<int:book_pk>/create/', views.ReviewCreateView.as_view(), name='create'),
    path('<int:pk>/', views.ReviewDetailView.as_view(), name='detail'),
    path('<int:review_pk>/comment/', views.CommentCreateView.as_view(), name='comment_create'),
]