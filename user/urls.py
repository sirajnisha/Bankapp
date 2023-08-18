from django.urls import include, path

from . import views
appname ='user'
urlpatterns = [
    path('', views.UserListView.as_view(), name='user_changelist'),
    path('add/', views.UserCreateView.as_view(), name='user_add'),
    path('<int:pk>/', views.UserUpdateView.as_view(), name='user_change'),
    path('ajax/load-branches/', views.load_branches, name='ajax_load_branches'),
   ]