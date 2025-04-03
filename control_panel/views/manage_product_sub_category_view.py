from django.shortcuts import render, redirect
from django.views import View
from ..forms import ManageProductSubCategoryForm
from ..models import ProductSubCategoryModel  # Import the ProductSubCategory model
from django.contrib import messages


class ManageProductSubCategoryListView(View):
    def get(self, request):
        subcategories = ProductSubCategoryModel.objects.all()
        form = ManageProductSubCategoryForm()
        return render(request, 'admin/manage_product_sub_category.html', {"subcategories": subcategories, "form": form})


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
