from django.urls import path

from demo.api import views

urlpatterns = [
    path('login/', views.login),
    path('reviews/', views.get_reviews),
    path('reviews/<int:pk>/', views.get_by_id)
]
