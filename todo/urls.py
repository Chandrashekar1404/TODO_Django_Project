
from django.urls import path,include

from . import views

urlpatterns = [
    # TO DO

    # to add the task
    path('addtask/',views.addTask, name='addTask' ),

    #to markasdone
    path('mark_as_done/<int:pk>/',views.mark_as_done, name='mark_as_done'),


    # Edit feature
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task')
]
