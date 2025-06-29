from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib import messages
from django.db.models import Sum
from .models import SalesBill
from .forms import SalesBillForm

# List view – Display, filter, paginate, and sum Sales Bills
def sales_bill_list(request):
    query = request.GET.get("q", "")
    sales_bills = SalesBill.objects.all().order_by("id")
    
    if query:
        sales_bills = sales_bills.filter(project_name__name_of_project__icontains=query)

    paginator = Paginator(sales_bills, 10)
    page_number = request.GET.get("page")
    try:
        page_obj = paginator.get_page(page_number)
    except (PageNotAnInteger, EmptyPage):
        page_obj = paginator.get_page(1)

    total_bill = sales_bills.aggregate(total=Sum('bill_amount'))['total'] or 0

    return render(request, "sales_bill/sales_bill_list.html", {
        "sales_bills": page_obj,
        "query": query,
        "total_bill_amount": total_bill
    })

# Create/Update view – Handles both new and edit scenarios
def sales_bill_form(request, id=None):
    bill = get_object_or_404(SalesBill, id=id) if id else None
    if request.method == "POST":
        form = SalesBillForm(request.POST, instance=bill)
        if form.is_valid():
            form.save()
            messages.success(request, "Sales Bill saved successfully.")
            return redirect("sales_bill_list")
    else:
        form = SalesBillForm(instance=bill)

    return render(request, "sales_bill/sales_bill_form.html", {"form": form})

# Delete view – Removes a SalesBill entry
def sales_bill_delete(request, id):
    sales_bill = get_object_or_404(SalesBill, id=id)
    sales_bill.delete()
    messages.warning(request, f"Sales Bill '{sales_bill.project_name.name_of_project}' deleted.")
    return redirect("sales_bill_list")


