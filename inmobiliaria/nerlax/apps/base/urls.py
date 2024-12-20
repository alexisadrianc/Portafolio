from django.urls import path
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', Login.as_view(), name="login"),
    path('register/', UsersRegister, name='register'),
    path('logout/', login_required(logoutUser), name='logout'),

    path('list_user/', login_required(ListUsers.as_view()), name='list-users'),
    path('create/', login_required(CreateUsers.as_view()), name='create-users'),
    path('edit/<int:pk>', login_required(UpdateUsers.as_view()), name='update-users'),
    path('delete/<int:pk>', login_required(DeleteUsers.as_view()), name='delete-users'),
    path('profile/<int:pk>', login_required(DetailUser.as_view()), name='profile-users'),

    path('list-company/', login_required(ListCompany.as_view()), name='list-company'),
    path('create-company/', login_required(CreateCompany.as_view()), name='create-company'),
    path('update-company/<int:pk>', login_required(UpdateCompany.as_view()), name='edit-company'),
    path('delete-company/<int:pk>', login_required(DeleteCompany.as_view()), name='delete-company'),

    path('list-rol/', login_required(ListRol.as_view()), name='list-rol'),
    path('create-rol/', login_required(CreateRol.as_view()), name='create-rol'),
    path('update-rol/<int:pk>', login_required(UpdateRol.as_view()), name='edit-rol'),
    path('delete-rol/<int:pk>', login_required(DeleteRol.as_view()), name='delete-rol'),
]

# url de vista implicitas
urlpatterns += [
    path('users/', login_required(TemplateView.as_view(template_name='base/users.html')), name='users'),
    path('companies/', login_required(TemplateView.as_view(template_name='base/company.html')), name='companies'),
    path('roles/', login_required(TemplateView.as_view(template_name='base/rol.html')), name='roles'),

]
