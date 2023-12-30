from django.urls import path
from.import views

urlpatterns = [
    path('login', views.login, name = 'login'),
    path('signup', views.signup, name = 'signup'),
    path('home', views.home , name = 'home'),
    path('logout', views.logout, name = 'logout'),
    path('user_table', views.user_table, name = 'user_table'),
    path('delete/<int:id>', views.delete, name = 'delete'),
    path('update/<int:id>', views.update, name = 'update'),
]