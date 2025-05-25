from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from ..models import ProductCategoryModel
from ..forms import ManageProductCategoryForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView


#List
class ManageProductCategoryListView(View):
    def get(self, request):
        categories = ProductCategoryModel.objects.all()
        form = ManageProductCategoryForm()
        return render(request, 'admin/manage_product_category.html', {"categories": categories, "form": form})


# Create
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


# Update
class ManageProductCategoryEditView(UpdateView):
    model = ProductCategoryModel
    form_class = ManageProductCategoryForm
    success_url = reverse_lazy('manage_product_category_list')

    def form_invalid(self, form):
        categories = ProductCategoryModel.objects.all()
        return self.render_to_response(self.get_context_data(form=form, categories=categories))
    

# Delete
class ManageProductCategoryDeleteView(View):
    """Handles product category deletion."""

    def post(self, request, pk, *args, **kwargs):
        """Deletes a product category and redirects to the category list."""
        category = get_object_or_404(ProductCategoryModel, pk=pk)
        category.delete()
        messages.success(request, "Product category deleted successfully!")
        return redirect("manage_product_category_list")  # Ensure this is the correct URL name
    
# Toggle Button
class ManageToggleProductCategoryActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        category = get_object_or_404(ProductCategoryModel, pk=pk)
        category.is_active = not category.is_active
        category.save()

        status = "activated" if category.is_active else "deactivated"
        messages.success(request, f"Category '{category.name}' has been {status}.")
        
        return redirect('manage_product_category_list')
