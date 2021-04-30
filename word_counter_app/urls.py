from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('counter/', views.counter, name='counter'),
    path('delete_t1/', views.delete_t1, name='delete_t1'),
    path('delete_t2/', views.delete_t2, name='delete_t2'),
    path('delete_qc/', views.delete_qc, name='delete_qc'),
    path('add_t1/', views.add_t1, name='add_t1'),
    path('add_t2/', views.add_t2, name='add_t2'),
    path('add_qc/', views.add_qc, name='add_qc'),
]
