from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Resource
from .forms import ResourceForm

# 🧠 CREATE + UPDATE + LIST
def resource_fl_view(request, id=None):
    resource = None
    if id:
        try:
            resource = Resource.objects.get(id=id)
        except Resource.DoesNotExist:
            messages.error(request, f"⚠️ Resource with ID {id} not found.")
            return redirect("resource_fl")

    form = ResourceForm(request.POST or None, instance=resource)

    if request.method == "POST":
        if form.is_valid():
            saved = form.save()
            action = "Updated" if id else "Created"
            messages.success(request, f"✅ {action} resource: '{saved.name_of_resource}'")
            return redirect("resource_fl")
        else:
            messages.error(request, "⚠️ Please correct the errors in the form.")

    # 🔍 Search and paginate resources
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

# ❌ DELETE
def resource_delete(request, id):
    resource = get_object_or_404(Resource, id=id)
    resource.delete()
    messages.warning(request, f"🗑️ Deleted resource: '{resource.name_of_resource}'.")
    return redirect("resource_fl")


