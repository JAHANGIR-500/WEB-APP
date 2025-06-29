from django.urls import path
from .views import (
    work_plan_list,
    work_plan_form,
    work_plan_delete,
    gantt_chart_data,  # ✅ Now included directly
)

urlpatterns = [
    path("", work_plan_list, name="work_plan_list"),                         # Display work plan list
    path("form/", work_plan_form, name="work_plan_create"),                 # Create new
    path("form/<int:id>/", work_plan_form, name="work_plan_edit"),          # Edit existing
    path("delete/<int:id>/", work_plan_delete, name="work_plan_delete"),    # Delete
    path("work-plan/gantt-data/", gantt_chart_data, name="gantt_chart_data"),  # ✅ Gantt JSON endpoint
]






