from django.urls import path
from .views import *

urlpatterns = [
    path('', todoListAPI,name="todoListAPI"),
    path('todo/<int:id>', todoDetailsAPI,name="todoListAPI"),
]
