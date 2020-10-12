"""company URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register-user', views.register_user, name='register-user'),
    path('list-user', views.list_user, name='list-user'),
    path('view-user/<int:id>', views.view_user, name='view-user'),
    path('edit-user/<int:id>', views.edit_user, name='edit-user'),
    path('delete-user/<int:id>', views.delete_user, name='delete-user'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('change-password', views.change_password, name='change-password'),
    path('profile', views.profile_view, name='profile'),
]
