from django.urls import path
from .views import resource_fl_view, resource_delete
urlpatterns = [
    path("", resource_fl_view, name="resource_fl"),                  # 👈 CREATE + LIST view
    path("<int:id>/", resource_fl_view, name="resource_edit"),       # ✏️ Edit a resource
    path("delete/<int:id>/", resource_delete, name="resource_delete")# ❌ Delete a resource
]
