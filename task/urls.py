from django.urls import path
from .views import task_list, task_form, task_delete
urlpatterns = [
    path("", task_list, name="task_list"),                   # Display task list with filtering and pagination
    path("form/", task_form, name="task_create"),            # Create a new task
    path("form/<int:id>/", task_form, name="task_edit"),     # Edit an existing task
    path("delete/<int:id>/", task_delete, name="task_delete"),  # Delete a task
]
