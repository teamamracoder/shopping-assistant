from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from ..models import ProductCategoryModel
from ..forms import ManageProductCategoryForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.forms import ValidationError
from ..models import ProductCategoryModel
from ..forms import ManageProductCategoryForm
from services.product_category_service import ProductCategoryModelService


category_service = ProductCategoryModelService()

# List View
class ManageProductCategoryListView(View):
    def get(self, request):
        categories = category_service.get_all_categories()
        form = ManageProductCategoryForm()
        return render(request, 'admin/manage_product_category.html', {
            "categories": categories,
            "form": form
        })

# Create View
class ManageProductCategoryCreateView(View):
    def post(self, request):
        form = ManageProductCategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                if not isinstance(request.user, AnonymousUser):
                    data['created_by'] = request.user
                    data['updated_by'] = request.user
                category_service.create_category(data)
                messages.success(request, "Category added successfully!")
                return redirect('manage_product_category_list')
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.success(request, "Category added successfully!")

        categories = category_service.get_all_categories()
        return render(request, "admin/manage_product_category.html", {
            "form": form,
            "categories": categories
        })

# Update View
class ManageProductCategoryEditView(UpdateView):
    model = ProductCategoryModel
    form_class = ManageProductCategoryForm
    success_url = reverse_lazy('manage_product_category_list')

    def form_valid(self, form):
        category = self.get_object()
        data = form.cleaned_data
        if not isinstance(self.request.user, AnonymousUser):
            data['updated_by'] = self.request.user
        try:
            category_service.update_category(category, data)
            messages.success(self.request, "Category updated successfully!")
        except ValidationError as e:
            messages.error(self.request, str(e))
        return super().form_valid(form)

    def form_invalid(self, form):
        categories = category_service.get_all_categories()
        return self.render_to_response(self.get_context_data(form=form, categories=categories))
    

# Delete View
class ManageProductCategoryDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        category = category_service.get_category_by_id(pk)
        if not category:
            messages.error(request, "Category not found.")
            return redirect("manage_product_category_list")

        try:
            category_service.delete_category(category)
            messages.success(request, "Product category deleted successfully!")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_product_category_list")    


# Toggle Active Status
class ManageToggleProductCategoryActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        category = category_service.get_category_by_id(pk)
        if not category:
            messages.error(request, "Category not found.")
            return redirect("manage_product_category_list")

        try:
            new_status = not category.is_active
            category_service.update_category(category, {'is_active': new_status})
            status_text = "activated" if new_status else "deactivated"
            messages.success(request, f"Category '{category.name}' has been {status_text}.")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_product_category_list")
    
    