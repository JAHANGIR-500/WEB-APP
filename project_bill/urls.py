from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_bill_list, name="project_bill_list"),
    path("form/", views.project_bill_form, name="project_bill_create"),
    path("form/<int:id>/", views.project_bill_form, name="project_bill_edit"),
    path("delete/<int:id>/", views.project_bill_delete, name="project_bill_delete"),

    # Select2 AJAX endpoints
    path("autocomplete/project/", views.ProjectAutocomplete.as_view(), name="project-autocomplete"),
    path("autocomplete/contractor/", views.ContractorAutocomplete.as_view(), name="contractor-autocomplete"),
]


