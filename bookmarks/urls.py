from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('update/<bookmark_id>', views.update, name='update'),
    path('delete/<bookmark_id>', views.delete, name='delete')
]