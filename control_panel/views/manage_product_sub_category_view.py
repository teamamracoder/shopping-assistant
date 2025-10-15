from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.forms import ValidationError
from ..forms import ManageProductSubCategoryForm
from services.product_sub_category_service import ProductSubCategoryModelService
from utils.common_utils import get_user_id


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
        print("[DEBUG] Current user:", get_user_id(request))
        form = ManageProductSubCategoryForm(request.POST)
        if form.is_valid():
            subcategory = form.save(commit=False)  # get instance without saving

            # Assign created_by and updated_by
            user_id = get_user_id(request)
            subcategory.created_by = user_id
            subcategory.updated_by = user_id

            try:
                subcategory.save()
                messages.success(request, "Subcategory added successfully!", extra_tags="subcategory")
                return redirect("manage_product_sub_category_list")
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        subcategories = subcategory_service.get_all_sub_categories()
        return render(request, "admin/manage_product_sub_category.html", {
            "form": form,
            "subcategories": subcategories
        })



# Edit View
class ManageProductSubCategoryEditView(View):
    def post(self, request, *args, **kwargs):
        subcategory_id = kwargs.get('pk') or request.POST.get('subcategory_id')
        if not subcategory_id:
            messages.error(request, "Subcategory ID is missing.")
            return redirect('manage_product_sub_category_list')

        instance = subcategory_service.get_sub_category_by_id(subcategory_id)
        if not instance:
            messages.error(request, "Subcategory not found.")
            return redirect('manage_product_sub_category_list')

        form = ManageProductSubCategoryForm(request.POST, instance=instance)
        if form.is_valid():
            subcategory = form.save(commit=False)

            # Assign updated_by
            subcategory.updated_by = get_user_id(request)

            try:
                subcategory.save()
                messages.success(request, "Subcategory updated successfully!", extra_tags="subcategory")
                return redirect('manage_product_sub_category_list')
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        subcategories = subcategory_service.get_all_sub_categories()
        return render(request, 'admin/manage_product_sub_category.html', {
            'form': form,
            'subcategories': subcategories
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