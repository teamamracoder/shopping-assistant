import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from ..forms import ManageStoreForm
from services.store_service import storeModelService
from django.core.exceptions import ValidationError

store_service = storeModelService()

# List View
class ManageStoreListView(View):
    def get(self, request):
        stores = store_service.get_all_stores()
        print(stores)
        form = ManageStoreForm()
        return render(request, 'admin/manage_store.html', {"stores": stores, "form": form,
        })


# Create View
class ManageStoreCreateView(View):
    def get(self, request): 
        form = ManageStoreForm()
        stores = store_service.get_all_stores()
        return render(request, "admin/manage_store.html", {"form": form, "stores": stores})

    def post(self, request):
        form = ManageStoreForm(request.POST)

        if form.is_valid():
            store_data = form.cleaned_data

            # Owner and user info
            store_data['owner_id'] = 1  # Default owner_id or use request.user.id if appropriate
            if not isinstance(request.user, AnonymousUser):
                store_data['created_by'] = request.user
                store_data['updated_by'] = request.user

            # File uploads
            store_image_urls = []
            for f in request.FILES.getlist('store_images'):
                save_dir = os.path.join(settings.MEDIA_ROOT, 'img/store')
                os.makedirs(save_dir, exist_ok=True)
                save_path = os.path.join(save_dir, f.name)
                with open(save_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                relative_url = f'media/img/store/{f.name}'
                store_image_urls.append(relative_url)

            store_data['store_image_urls'] = store_image_urls

            try:
                store_service.create_store(store_data)
                messages.success(request, "Store added successfully!")
                return redirect("manage_store_list")
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        return render(request, "admin/manage_store.html", {
            "form": form,
            "stores": store_service.get_all_stores()
        })


# Edit View
class ManageStoreEditView(View):
    def post(self, request, pk):
        store = store_service.get_store_by_id(pk)
        if not store:
            messages.error(request, "Store not found.")
            return redirect("manage_store_list")

        form = ManageStoreForm(request.POST, request.FILES, instance=store)

        if form.is_valid():
            updated_data = form.cleaned_data

            # Handle image uploads
            store_image_urls = store.store_image_urls or []

            for f in request.FILES.getlist('store_images'):
                save_dir = os.path.join(settings.MEDIA_ROOT, 'img/store')
                os.makedirs(save_dir, exist_ok=True)
                save_path = os.path.join(save_dir, f.name)
                with open(save_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                relative_url = f'media/img/store/{f.name}'
                store_image_urls.append(relative_url)

            updated_data['store_image_urls'] = store_image_urls

            if not isinstance(request.user, AnonymousUser):
                updated_data['updated_by'] = request.user

            try:
                store_service.update_store(store, updated_data)
                messages.success(request, "Store updated successfully!")
                return redirect("manage_store_list")
            except ValidationError as e:
                messages.error(request, str(e))

        messages.error(request, "Please correct the errors below.")
        return render(request, "admin/manage_store.html", {
        "form": form,
        "stores": store_service.get_all_stores(),
    })



# Delete View
class ManageStoreDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        store = store_service.get_store_by_id(pk)
        if not store:
            messages.error(request, "Store not found.")
            return redirect("manage_store_list")

        try:
            store_service.delete_store(store)
            messages.success(request, "Store deleted successfully!")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_store_list")


# Toggle Active/Inactive
class ManageToggleStoreActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        store = store_service.get_store_by_id(pk)
        if not store:
            messages.error(request, "Store not found.")
            return redirect("manage_store_list")

        new_status = not store.is_active
        try:
            store_service.update_store(store, {"is_active": new_status})
            status = "activated" if new_status else "deactivated"
            messages.success(request, f"Store '{store.store_name}' has been {status}.")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_store_list")
