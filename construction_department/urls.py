from django.urls import include, path
from .views import construction_department_view

urlpatterns = [
    path('', construction_department_view, name='construction_department'),

    # 💼 Submodules neatly routed:
    path('project/', include('project.urls')),
    path('customer/', include('customer.urls')),
    path('sales_bill/', include('sales_bill.urls')),
    path('resource/', include('resource.urls')),
]









