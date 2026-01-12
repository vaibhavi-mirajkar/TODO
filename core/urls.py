from django.urls import path
from .views import todo_home,complete_todo,delete_todo,todo_edit 


urlpatterns = [
    path('',todo_home,name='todo_home'),
    path('complete/<int:todo_id>/', complete_todo, name='complete_todo'),
    path("delete/<int:todo_id>/", delete_todo, name="delete_todo"),
    path("edit/<int:todo_id>/", todo_edit, name="todo_edit"),
]

