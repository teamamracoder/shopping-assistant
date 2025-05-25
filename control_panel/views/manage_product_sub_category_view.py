from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from ..forms import ManageProductSubCategoryForm
from ..models import ProductSubCategoryModel  # Import the ProductSubCategory model
from django.contrib import messages
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView


#List
class ManageProductSubCategoryListView(View):
    def get(self, request):
        subcategories = ProductSubCategoryModel.objects.all()
        form = ManageProductSubCategoryForm()
        return render(request, 'admin/manage_product_sub_category.html', {"subcategories": subcategories, "form": form})

#Create
class ManageProductSubCategoryCreateView(View):
    def get(self, request):
        """Handle GET request before data retrieval."""
        form = ManageProductSubCategoryForm()
        subcategories = ProductSubCategoryModel.objects.all()
        return render(request, "admin/manage_product_sub_category.html", {
            "form": form,
            "subcategories": subcategories
        })

    def post(self, request):
        """Handle form submission and save data to the database."""
        form = ManageProductSubCategoryForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            return redirect("manage_product_sub_category_list")  # Ensure URL name matches

        # If the form is invalid, reload with existing subcategories
        subcategories = ProductSubCategoryModel.objects.all()
        return render(request, "admin/manage_product_sub_category.html", {
            "form": form,
            "subcategories": subcategories
        })


# class ManageProductSubCategoryEditView(View):
#     def post(self, request, *args, **kwargs):
#         subcategory_id = request.POST.get('subcategory_id')  # Corrected key name
#         instance = None

#         if subcategory_id:
#             instance = get_object_or_404(ProductSubCategoryModel, pk=subcategory_id)

#         form = ManageProductSubCategoryForm(request.POST, instance=instance)

#         if form.is_valid():
#             form.save()
#             return redirect('manage_product_sub_category_list')
#         else:
#             return render(request, 'control_panel/product_subcategory_list.html', {
#                 'form': form,
#                 'subcategories': ProductSubCategoryModel.objects.all(),
#                 'errors': form.errors
#             })


class ManageProductSubCategoryEditView(View):
    def post(self, request, *args, **kwargs):
        subcategory_id = kwargs.get('pk') or request.POST.get('subcategory_id')
        instance = None

        if subcategory_id:
            instance = get_object_or_404(ProductSubCategoryModel, pk=subcategory_id)

        form = ManageProductSubCategoryForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            return redirect('manage_product_sub_category_list')
        else:
            return render(request, 'control_panel/product_subcategory_list.html', {
                'form': form,
                'subcategories': ProductSubCategoryModel.objects.all(),
                'errors': form.errors
            })
#Delete
class ManageProductSubCategoryDeleteView(View):
    """Handles product subcategory deletion."""

    def post(self, request, pk, *args, **kwargs):
        subcategories = get_object_or_404(ProductSubCategoryModel, pk=pk)
        subcategories.delete()
        messages.success(request, "Product Sub Category deleted successfully!")
        return redirect("manage_product_sub_category_list")  # Ensure this URL name is correct
    
# Toggle Button
class ManageToggleProductSubCategoryActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        subcategory = get_object_or_404(ProductSubCategoryModel, pk=pk)
        subcategory.is_active = not subcategory.is_active
        subcategory.save()

        status = "activated" if subcategory.is_active else "deactivated"
        messages.success(request, f"Subcategory '{subcategory.name}' has been {status}.")
        
        return redirect('manage_product_sub_category_list')