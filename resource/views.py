from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Resource
from .forms import ResourceForm

# 🧠 Unified view: Form + List (resource_fl.html)
def resource_fl_view(request, id=None):
    # Handle editing if ID is passed
    resource = get_object_or_404(Resource, id=id) if id else None
    form = ResourceForm(request.POST or None, instance=resource)
    # Handle form submission
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Resource saved successfully.")
        return redirect("resource_fl")
    # Handle filtering and pagination
    query = request.GET.get("q", "")
    resources = Resource.objects.all().order_by("id")
    if query:
        resources = resources.filter(name_of_resource__icontains=query)
    paginator = Paginator(resources, 10)
    page_number = request.GET.get("page")
    try:
        resources_page = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        resources_page = paginator.get_page(1)
    return render(request, "resource/resource_fl.html", {
        "form": form,
        "resources": resources_page,
        "query": query,
        "edit_id": id
    })
# ❌ Delete view remains unchanged
def resource_delete(request, id):
    resource = get_object_or_404(Resource, id=id)
    messages.warning(request, f"Resource '{resource.name_of_resource}' deleted.")
    resource.delete()
    return redirect("resource_fl")

