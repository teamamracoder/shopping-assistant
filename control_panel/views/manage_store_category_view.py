from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from ..models import StoreCategoryModel
from ..forms import ManageStoreCategoryForm
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.forms import ValidationError
from ..models import StoreCategoryModel
from services.store_category_service import StoreCategoryService

store_category_service = StoreCategoryService()

class ManageStoreCategoryListView(View):
    def get(self, request):
        store_categories = store_category_service.get_all_store_categories()
        form = ManageStoreCategoryForm()
        return render(request, 'admin/manage_store_category.html', {
            "categories": store_categories,
            "form": form
        })

# Create View
class ManageStoreCategoryCreateView(View):
    def post(self, request):
        form = ManageStoreCategoryForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            try:
                if not isinstance(request.user, AnonymousUser):
                    data['created_by'] = request.user
                    data['updated_by'] = request.user
                store_category_service.create_store_category(data)
                messages.success(request, "Store category added successfully!")
                return redirect('manage_store_category_list')
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            messages.success(request, "Store Category added successfully!")

        store_categories = store_category_service.get_all_store_categories()
        return render(request, 'admin/manage_store_category.html', {
            "form": form,
            "categories": store_categories
        })

# Update View
class ManageStoreCategoryEditView(UpdateView):
    model = StoreCategoryModel
    form_class = ManageStoreCategoryForm
    success_url = reverse_lazy('manage_store_category_list')

    def form_valid(self, form):
        store_category = self.get_object()
        data = form.cleaned_data
        if not isinstance(self.request.user, AnonymousUser):
            data['updated_by'] = self.request.user        
        try:
            store_category_service.update_store_category(store_category, data)
            messages.success(self.request, "Store category updated successfully!")
        except ValidationError as e:
            messages.error(self.request, str(e))
        return super().form_valid(form)

    def form_invalid(self, form):
        store_categories = store_category_service.get_all_store_categories()
        return self.render_to_response(self.get_context_data(form=form, store_categories=store_categories))

# Delete View
class ManageStoreCategoryDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        store_category = store_category_service.get_store_category_by_id(pk)
        if not store_category:
            messages.error(request, "Store category not found.")
            return redirect("manage_store_category_list")

        try:
            store_category_service.delete_store_category(store_category)
            messages.success(request, "Store category deleted successfully!")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_store_category_list")

# Toggle Active Status
class ManageToggleStoreCategoryActiveView(View):
    def post(self, request, pk):
        category = store_category_service.get_store_category_by_id(pk)
        if not category:
            messages.error(request, "Store category not found.")
            return redirect("manage_store_category_list")

        try:
            new_status = not category.is_active
            store_category_service.update_store_category(category, {'is_active': new_status})
            status = "activated" if new_status else "deactivated"
            messages.success(request, f"Category '{category.name}' has been {status}.")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_store_category_list")
