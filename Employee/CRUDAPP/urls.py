from django.urls import path
from . import views

urlpatterns=[
    path('', views.homepage, name='homepage'),
    path('insert/', views.insert_emp, name='insert-emp'),
    path('show/', views.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
    path('about/' , views.about , name='about'),
]