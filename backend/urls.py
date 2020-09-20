from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('snacks', views.snacks, name='snacks'),
    path('balance/<int:user_id>', views.balance, name='balance'),
]
