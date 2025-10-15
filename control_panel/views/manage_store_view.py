import os
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from ..forms import ManageStoreForm
from services.store_service import storeModelService
from django.core.exceptions import ValidationError
from decorators.validator import role_required
from constants import Role
from utils.common_utils import get_user_id

store_service = storeModelService()

## Store List View ##
class ManageStoreListView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request):
        stores = store_service.get_all_stores()
        form = ManageStoreForm()
        return render(request, 'admin/manage_store.html', {"stores": stores, "form": form,
        })


## Create View ##
class ManageStoreCreateView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request): 
        form = ManageStoreForm()
        stores = store_service.get_all_stores()
        return render(request, "admin/manage_store.html", {"form": form, "stores": stores})

    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request):
        print("[DEBUG] Current user:", get_user_id(request))
        # print("[DEBUG] Is authenticated:", request.user.is_authenticated)

        form = ManageStoreForm(request.POST, request.FILES)
        if form.is_valid():
            store = form.save(commit=False)  

            # if request.user.is_authenticated:
            store.created_by = get_user_id(request)
            store.updated_by = get_user_id(request)

            # Handle images
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

            store.store_image_urls = store_image_urls

            try:
                store.save()
                messages.success(request, "Store added successfully!", extra_tags='store')
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


## Edit View ##
class ManageStoreEditView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    
    def post(self, request, pk):
        print("[DEBUG] Current user:", get_user_id(request))
        store = store_service.get_store_by_id(pk)
        if not store:
            messages.error(request, "Store not found.")
            return redirect("manage_store_list")

        form = ManageStoreForm(request.POST, request.FILES, instance=store)

        if form.is_valid():
            store = form.save(commit=False)

            # if request.user.is_authenticated:
            store.updated_by = get_user_id(request)

            # image handle
            if request.FILES.getlist('store_images'):
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
                store.store_image_urls = store_image_urls

            store.save()
            messages.success(request, "Store updated successfully!", extra_tags='store')
            return redirect("manage_store_list")

        messages.error(request, "Please correct the errors below.")
        return render(request, "admin/manage_store.html", {
            "form": form,
            "stores": store_service.get_all_stores(),
        })


## Delete View ##
class ManageStoreDeleteView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk, *args, **kwargs):
        store = store_service.get_store_by_id(pk)
        if not store:
            messages.error(request, "Store not found.")
            return redirect("manage_store_list")

        try:
            store_service.delete_store(store)
            messages.success(request, "Store deleted successfully!", extra_tags='store')
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_store_list")


## Toggle Active/Inactive ##
class ManageToggleStoreActiveView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk, *args, **kwargs):
        
        print("[DEBUG] Current user:", request.user)
        print("[DEBUG] Is authenticated:", request.user.is_authenticated)
        
        try:
            store = store_service.toggle_store_status(pk, updated_by=request.user)
            if store.is_active:
                messages.success(request, f"Store '{store.store_name}' has been activated successfully!", extra_tags="store")
            else:
                messages.success(request, f"Store '{store.store_name}' has been deactivated successfully!", extra_tags="store")
        except ValidationError as e:
            messages.error(request, str(e), extra_tags="store")

        return redirect("manage_store_list")