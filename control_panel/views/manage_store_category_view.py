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
from utils.common_utils import get_user_id


store_category_service = StoreCategoryService()

##Store Category List ##
class ManageStoreCategoryListView(View):
    def get(self, request):
        store_categories = store_category_service.get_all_store_categories()
        form = ManageStoreCategoryForm()
        return render(request, 'admin/manage_store_category.html', {
            "categories": store_categories,
            "form": form
        })


## Create View ##
class ManageStoreCategoryCreateView(View):
    def get(self, request):
        form = ManageStoreCategoryForm()
        categories = store_category_service.get_all_store_categories()
        return render(request, 'admin/manage_store_category.html', {"form": form, "categories": categories})

    def post(self, request):
        print("[DEBUG] Current user:", get_user_id(request))

        form = ManageStoreCategoryForm(request.POST)
        if form.is_valid():
            store_category = form.save(commit=False)  # don't save yet

            # Assign created_by and updated_by
            current_user_id = get_user_id(request)
            store_category.created_by = current_user_id
            store_category.updated_by = current_user_id

            try:
                store_category.save()
                messages.success(request, "Store category added successfully!", extra_tags='store_category')
                return redirect('manage_store_category_list')
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        # Re-render form with existing categories
        categories = store_category_service.get_all_store_categories()
        return render(request, 'admin/manage_store_category.html', {
            "form": form,
            "categories": categories
        })


## Update View ##
class ManageStoreCategoryEditView(UpdateView):
    model = StoreCategoryModel
    form_class = ManageStoreCategoryForm
    success_url = reverse_lazy('manage_store_category_list')

    def form_valid(self, form):
        store_category = form.save(commit=False)  # get instance but don't save yet
       
        original = StoreCategoryModel.objects.get(pk=self.object.pk)
        store_category.created_by = original.created_by

        # Assign updated_by
        store_category.updated_by = get_user_id(self.request)

        try:
            store_category.save()  # save the instance
            store_category.updated_by = get_user_id(self.request)
            messages.success(self.request, "Store category updated successfully!", extra_tags='store_category')
        except ValidationError as e:
            messages.error(self.request, str(e))
            return self.form_invalid(form)

        return super().form_valid(form)

    def form_invalid(self, form):
        store_categories = store_category_service.get_all_store_categories()
        return self.render_to_response(self.get_context_data(form=form, store_categories=store_categories))


## Delete View ##
class ManageStoreCategoryDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        store_category = store_category_service.get_store_category_by_id(pk)
        if not store_category:
            messages.error(request, "Store category not found.")
            return redirect("manage_store_category_list")

        try:
            store_category_service.delete_store_category(store_category)
            messages.success(request, "Store category deleted successfully!", extra_tags='store_category')
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_store_category_list")


## Toggle Active Status ##
class ManageToggleStoreCategoryActiveView(View):
    def post(self, request, pk):
        try:
            category = store_category_service.toggle_store_category_status(pk, updated_by=request.user)
            status = "activated" if category.is_active else "deactivated"
            # Add a custom tag for SweetAlert
            messages.success(request, f"Category '{category.name}' has been {status}.", extra_tags='store_category')
        except ValidationError as e:
            messages.error(request, str(e), extra_tags='store_category')

        return redirect("manage_store_category_list")
