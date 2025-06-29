from django.urls import include, path
from .views import design_department_view
urlpatterns = [
    path('', design_department_view, name='design_department'),
    path('task/', include('task.urls')),  # ✅ Ensures tasks are accessible
    path('employee/', include('employee.urls')),  # ✅ Ensures tasks are accessible
    path('work_plan/', include('work_plan.urls')),  # ✅ Ensures tasks are accessible
]


