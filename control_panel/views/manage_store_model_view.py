from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models import StoreModel
from ..forms.manage_store_model_form import *


class ManageStoreListView(View):
    def get(self, request):
        stores = StoreModel.objects.select_related('owner', 'store_category').all().order_by('-created_at')
        form = StoreForm()
        return render(request, 'admin/manage_store_model.html', {'stores': stores, 'form': form})


class ManageCreateStoreView(View):
    def post(self, request):
        form = StoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            if request.user.is_authenticated:
                store.created_by = request.user
                store.updated_by = request.user
            store.save()
            messages.success(request, "Store created successfully.")
        else:
            messages.error(request, f"Failed to create store: {form.errors}")
        return redirect('manage_Store_list')


from django.shortcuts import get_object_or_404


class ManageUpdateStoreView(View):
    def post(self, request, pk):
        store = get_object_or_404(StoreModel, pk=pk)
        form = StoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            messages.success(request, "Store updated successfully.")
            return redirect('manage_Store_list')
        else:
            messages.error(request, "Please correct the errors below.")


            store_list = StoreModel.objects.all()
            return render(request, "admin/manage_store_model.html", {
                "form": form,
                "store_list": store_list,
                "store": store,  # Ensure the store object is passed
            })            


class ToggleStoreStatus(View):
    def post(self, request, store_id):
        store = get_object_or_404(StoreModel, id=store_id)
        store.is_active = not store.is_active
        store.save()
        status = "activated" if store.is_active else "deactivated"
        messages.success(request, f"Store '{store.store_name}' has been {status}.")
        return redirect('manage_Store_list')
