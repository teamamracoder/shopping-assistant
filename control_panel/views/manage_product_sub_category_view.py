from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.forms import ValidationError
from ..forms import ManageProductSubCategoryForm
from services.product_sub_category_service import ProductSubCategoryModelService


subcategory_service = ProductSubCategoryModelService()

# List View
class ManageProductSubCategoryListView(View):
    def get(self, request):
        subcategories = subcategory_service.get_all_sub_categories()
        form = ManageProductSubCategoryForm()
        return render(request, 'admin/manage_product_sub_category.html', {
            "subcategories": subcategories,
            "form": form
        })


# Create View
class ManageProductSubCategoryCreateView(View):
    def get(self, request):
        form = ManageProductSubCategoryForm()
        subcategories = subcategory_service.get_all_sub_categories()
        return render(request, "admin/manage_product_sub_category.html", {
            "form": form,
            "subcategories": subcategories
        })

    def post(self, request):
        form = ManageProductSubCategoryForm(request.POST)
        if form.is_valid():
            try:
                subcategory_service.create_sub_category(form.cleaned_data)
                messages.success(request, "Subcategory added successfully!")
                return redirect("manage_product_sub_category_list")
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Please correct the errors below.")

        subcategories = subcategory_service.get_all_sub_categories()
        return render(request, "admin/manage_product_sub_category.html", {
            "form": form,
            "subcategories": subcategories
        })


# Edit View
class ManageProductSubCategoryEditView(View):
    def post(self, request, *args, **kwargs):
        subcategory_id = kwargs.get('pk') or request.POST.get('subcategory_id')
        instance = None

        if subcategory_id:
            instance = subcategory_service.get_sub_category_by_id(subcategory_id)
            if not instance:
                messages.error(request, "Subcategory not found.")
                return redirect('manage_product_sub_category_list')

        form = ManageProductSubCategoryForm(request.POST, instance=instance)
        if form.is_valid():
            try:
                subcategory_service.update_sub_category(instance, form.cleaned_data)
                messages.success(request, "Subcategory updated successfully!")
                return redirect('manage_product_sub_category_list')
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Please correct the errors below.")

        return render(request, 'admin/manage_product_sub_category.html', {
            'form': form,
            'subcategories': subcategory_service.get_all_sub_categories()
        })


# Delete View
class ManageProductSubCategoryDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        subcategory = subcategory_service.get_sub_category_by_id(pk)
        if not subcategory:
            messages.error(request, "Subcategory not found.")
            return redirect("manage_product_sub_category_list")

        try:
            subcategory_service.delete_sub_category(subcategory)
            messages.success(request, "Subcategory deleted successfully!")
        except Exception as e:
            messages.error(request, f"Failed to delete subcategory: {str(e)}")

        return redirect("manage_product_sub_category_list")


# Toggle Active View
class ManageToggleProductSubCategoryActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        try:
            subcategory = subcategory_service.toggle_sub_category_status(pk)
            status_text = "activated" if subcategory.is_active else "deactivated"
            messages.success(request, f"Subcategory '{subcategory.name}' has been {status_text}.")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_product_sub_category_list")