from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('protected/', views.ProtectedView.as_view(), name='protected'),
    path('home/', views.home_view, name='home'),
]