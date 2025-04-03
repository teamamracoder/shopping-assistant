from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from ..models import ProductCategoryModel
from ..forms import ManageProductCategoryForm
from django.http import JsonResponse


class ManageProductCategoryListView(View):
    def get(self, request):
        categories = ProductCategoryModel.objects.all()
        form = ManageProductCategoryForm()
        return render(request, 'admin/manage_product_category.html', {"categories": categories, "form": form})

class ManageProductCategoryCreateView(View):
    def post(self, request):
        form = ManageProductCategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)

            # Only assign user if they are authenticated
            if not isinstance(request.user, AnonymousUser):
                category.created_by = request.user
                category.updated_by = request.user

            category.save()
            messages.success(request, "Category added successfully!")
            return redirect('manage_product_category_list')

        messages.error(request, "Please correct the errors below.")
        return render(request, "admin/manage_product_category.html", {"form": form})
    
    
class ManageProductCategoryDeleteView(View):
    """Handles product category deletion."""

    def post(self, request, pk, *args, **kwargs):
        """Deletes a product category and redirects to the category list."""
        category = get_object_or_404(ProductCategoryModel, pk=pk)
        category.delete()
        messages.success(request, "Product category deleted successfully!")
        return redirect("manage_product_category_list")  # Ensure this is the correct URL name