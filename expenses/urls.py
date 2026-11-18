from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('edit/<int:expense_id>/',views.edit_expense, name='edit_expense'),
    path('delete/<int:expense_id>/',views.delete_expense, name='delete_expense'),
    path('register/',views.register_view, name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='expenses/login.html'), name ='login'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),


]