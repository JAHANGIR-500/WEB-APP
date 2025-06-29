from django.urls import path
from .views import employee_list, employee_form, employee_delete
urlpatterns = [
    path("", employee_list, name="employee_list"),                       # Display employee list with filtering and pagination
    path("form/", employee_form, name="employee_create"),                # Create a new employee
    path("form/<int:id>/", employee_form, name="employee_edit"),         # Edit an existing employee
    path("delete/<int:id>/", employee_delete, name="employee_delete"),   # Delete an employee
]
