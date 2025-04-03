from django.shortcuts import render, redirect
from django.views import View
from ..forms import ProductSubCategoryCreateForm
from ..models import ProductSubCategoryModel  # Import the ProductSubCategory model
from django.contrib import messages
# Corrected import statement


# class ManageProductSubCategoryListView(View):
#     def get(self, request):
#         form = ProductSubCategoryCreateForm()
#         return render(request, "admin/manage_product_sub_category.html",{"form": form})
    
class ManageProductSubCategoryListView(View):
    def get(self, request):
        return render(request, 'admin/manage_product_sub_category.html')



# class ManageProductSubCategoryCreateView(View):
#     def get(self, request):
#         """Display the form for creating a new Product Sub Category."""
#         form = ProductSubCategoryCreateForm()
#         subcategories = manage_product_sub_category_service.get_all_subcategories()
#         return render(request, "admin/manage_product_sub_category.html", {
#             "form": form,
#             "subcategories": subcategories
#         })

#     def post(self, request):
#         """Handle form submission and create a new Product Sub Category."""
#         form = ProductSubCategoryCreateForm(request.POST)
#         if form.is_valid():
#             manage_product_sub_category_service.create_subcategory(
#                 form.cleaned_data["category"],
#                 form.cleaned_data["name"],
#                 form.cleaned_data["description"]
#             )
#             return redirect("manage_product_sub_category")  # Redirect to refresh the page
#         subcategories = manage_product_sub_category_service.get_all_subcategories()
#         return render(request, "admin/manage_product_sub_category.html", {
#             "form": form,
#             "subcategories": subcategories
#         })




class ManageProductSubCategoryListView(View):
    def get(self, request):
        """Display the form and existing subcategories."""
        form = ProductSubCategoryCreateForm()
        subcategories = ProductSubCategoryModel.objects.all()  # Fetch all subcategories
        return render(request, "admin/manage_product_sub_category.html", {
            "form": form,
            "subcategories": subcategories
        })


class ManageProductSubCategoryCreateView(View):
    def get(self, request):
        """Handle GET request before data retrieval."""
        form = ProductSubCategoryCreateForm()
        subcategories = ProductSubCategoryModel.objects.all()
        return render(request, "admin/manage_product_sub_category.html", {
            "form": form,
            "subcategories": subcategories
        })

    def post(self, request):
        """Handle form submission and save data to the database."""
        form = ProductSubCategoryCreateForm(request.POST)
        if form.is_valid():
            form.save()  # Save to database
            return redirect("manage_product_sub_category_list")  # Ensure URL name matches

        # If the form is invalid, reload with existing subcategories
        subcategories = ProductSubCategoryModel.objects.all()
        return render(request, "admin/manage_product_sub_category.html", {
            "form": form,
            "subcategories": subcategories
        })
