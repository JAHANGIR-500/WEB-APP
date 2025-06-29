from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from .models import Contractor
from .forms import ContractorForm

# List view – Display, filter, and paginate contractors
def contractor_list(request):
    query = request.GET.get("q", "")
    
    # Efficient filtering and ordering
    contractors = Contractor.objects.order_by("id")
    if query:
        contractors = contractors.filter(contractor_name__icontains=query)

    # Pagination setup
    paginator = Paginator(contractors, 10)
    page_number = request.GET.get("page")
    contractors_page = paginator.get_page(page_number)  # Django's get_page automatically handles errors

    return render(request, "contractor/contractor_list.html", {
        "contractors": contractors_page,
        "query": query
    })

# Create & Update view – Handle data entry form
def contractor_form(request, id=None):
    contractor = get_object_or_404(Contractor, id=id) if id else None

    if request.method == "POST":
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            messages.success(request, "Contractor saved successfully.")
            return redirect("contractor_list")
    else:
        form = ContractorForm(instance=contractor)

    return render(request, "contractor/contractor_form.html", {"form": form})

# Delete view – Remove contractor entry
def contractor_delete(request, id):
    contractor = get_object_or_404(Contractor, id=id)
    contractor.delete()
    messages.warning(request, f"Contractor '{contractor.contractor_name}' deleted.")
    return redirect("contractor_list")


