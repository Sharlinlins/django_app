from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.index, name='index'),
    path('home/', v.home, name='employee_home'),
    path('newemployee/', v.new_employee, name='employee_new'),
    path('manageemployee/<int:id>', v.manage_employee, name='employee_manage'),
    path('register/', v.register, name='register'),
    path('login/', v.login, name='login'),
    path('logout/', v.logout, name='logout'),
]
