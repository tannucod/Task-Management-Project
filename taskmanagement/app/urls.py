from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('login/', views.login, name="login"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('createtask/', views.create_task, name="createtask"),    
    path('viewtask/', views.view_task, name="viewtask"),    
    path('updatetask/<str:pk>/', views.update_task, name="updatetask"),    
    path('deletetask/<str:pk>/', views.delete_task, name="deletetask"),    
    path('deleteaccount/', views.delete_account, name="deleteaccount"),    
    path('logout/', views.user_logout, name="logout"),    

]