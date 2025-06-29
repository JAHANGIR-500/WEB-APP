from django.urls import path
from .views import sales_bill_list, sales_bill_form, sales_bill_delete
urlpatterns = [
    path("", sales_bill_list, name="sales_bill_list"),  # Display sales bill list with filtering and pagination
    path("form/", sales_bill_form, name="sales_bill_create"),  # Create a new sales bill
    path("form/<int:id>/", sales_bill_form, name="sales_bill_edit"),  # Edit an existing sales bill
    path("delete/<int:id>/", sales_bill_delete, name="sales_bill_delete"),  # Delete a sales bill
]
