from django.urls import path
from .views import contractor_list, contractor_form, contractor_delete
urlpatterns = [
    path("", contractor_list, name="contractor_list"),  # Display contractor list with filtering and pagination
    path("form/", contractor_form, name="contractor_create"),  # Create a new contractor
    path("form/<int:id>/", contractor_form, name="contractor_edit"),  # Edit an existing contractor
    path("delete/<int:id>/", contractor_delete, name="contractor_delete"),  # Delete a contractor
]
