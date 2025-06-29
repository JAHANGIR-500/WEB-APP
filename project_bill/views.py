from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from django_select2.views import Select2QuerySetView

from .models import ProjectBill, Project, Contractor
from .forms import ProjectBillForm


# 🔹 List with optional search
def project_bill_list(request):
    query = request.GET.get("q", "")
    bills = ProjectBill.objects.select_related("project", "contractor").order_by("-id")

    if query:
        bills = bills.filter(
            Q(work_name__icontains=query) |
            Q(project__name__icontains=query) |
            Q(contractor__company_name__icontains=query)
        )

    paginator = Paginator(bills, 10)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "project_bill/project_bill_list.html", {
        "project_bills": page_obj,
        "query": query
    })


# 🔹 Create or update a bill
def project_bill_form(request, id=None):
    bill = get_object_or_404(ProjectBill, id=id) if id else None
    form = ProjectBillForm(request.POST or None, instance=bill)

    if request.method == "POST":
        if form.is_valid():
            saved = form.save()
            messages.success(
                request,
                f"Project Bill for '{saved.work_name}' {'updated' if id else 'created'} successfully."
            )
            return redirect("project_bill_list")
        else:
            messages.error(request, "Please correct the errors below.")

    return render(request, "project_bill/project_bill_form.html", {"form": form})


# 🔹 Delete with confirmation
def project_bill_delete(request, id):
    bill = get_object_or_404(ProjectBill, id=id)

    if request.method == "POST":
        bill.delete()
        messages.warning(request, f"Bill for '{bill.work_name}' deleted.")
        return redirect("project_bill_list")

    return render(request, "project_bill/project_bill_confirm_delete.html", {"bill": bill})


# 🔍 Autocomplete endpoint: Project
class ProjectAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Project.objects.none()
        qs = Project.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs


# 🔍 Autocomplete endpoint: Contractor
class ContractorAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        if not self.request.user.is_authenticated:
            return Contractor.objects.none()
        qs = Contractor.objects.all()
        if self.q:
            qs = qs.filter(company_name__icontains=self.q)
        return qs



