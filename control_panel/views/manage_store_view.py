from django.shortcuts import render
from django.views import View
from ..forms .manage_store_form import *
from ..forms .manage_store_category_form import *
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from ..models import UserModel,StoreModel,StoreCategoryModel
from services import *
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.urls import reverse
from django.http import JsonResponse
from django.http import HttpResponseForbidden
import os
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.utils.timezone import now
from django.core.files.storage import default_storage
from django.conf import settings

class ManageStoreView(View):
    def get(self, request):
        form = ManageStoreForm()
        store_list = StoreModel.objects.all()
        # Split email strings into lists
        for store in store_list:
            if isinstance(store.email, str):
                store.email = store.email.split(',')
        return render(request, "admin/manage_store.html", {"form": form, "store_list": store_list})







IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif', '.webp']

class ManageCreateStore(View):
    def post(self, request, *args, **kwargs):
        form = ManageStoreForm(request.POST, request.FILES)

        if form.is_valid():
            store = form.save(commit=False)
            user_instance = get_object_or_404(UserModel, id=1)  # TODO: Replace with actual user logic
            store.is_active = True
            store.owner = user_instance
            store.created_by = user_instance
            store.updated_by = user_instance
            store.save()

            # Save images directly in media/ directory
            image_urls = []
            for f in request.FILES.getlist('store_images'):
                file_extension = os.path.splitext(f.name)[1].lower()
                if file_extension not in IMAGE_EXTENSIONS:
                    continue  # skip non-image files

                unique_timestamp = now().strftime('%Y%m%d%H%M%S')
                file_name = f"{unique_timestamp}_{f.name}"
                
                # Save directly into media/
                saved_path = default_storage.save(file_name, f)
                full_media_url = f"{settings.MEDIA_URL}{saved_path}"

                image_urls.append(full_media_url)

            store.store_image_urls = image_urls
            store.save()

            messages.success(request, "Store created successfully!")
            return redirect('manage_Store_list')
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "admin/manage_store.html", {"form": form})



# class ManageUpdateStoreView(View):
#     def post(self, request, pk):
#         store = get_object_or_404(StoreModel, pk=pk)
#         form = ManageStoreForm(request.POST, request.FILES, instance=store)

#         if form.is_valid():
#             updated_store = form.save(commit=False)

#             # Check if new image is uploaded
#             if 'store_images' in request.FILES:
#                 uploaded_file = request.FILES['store_images']
#                 save_path = os.path.join(settings.STATIC_ROOT, 'img/store', uploaded_file.name)
#                 os.makedirs(os.path.dirname(save_path), exist_ok=True)
#                 with open(save_path, 'wb+') as destination:
#                     for chunk in uploaded_file.chunks():
#                         destination.write(chunk)
#                 relative_url = f'static/img/store/{uploaded_file.name}'
#                 updated_store.store_images = relative_url

#             updated_store.save()
#             messages.success(request, "Store updated successfully!")
#             return redirect('manage_Store_list')
#         else:
#             store_list = StoreModel.objects.all()
#             messages.error(request, "Please correct the errors below.")
#             return render(request, "admin/manage_store.html", {"form": form, "store_list": store_list})
class ManageUpdateStoreView(View):
    def post(self, request, pk):
        store = get_object_or_404(StoreModel, pk=pk)
        form = ManageStoreForm(request.POST, request.FILES, instance=store)

        if form.is_valid():
            updated_store = form.save(commit=False)
            existing_urls = store.store_image_urls or []

            # Handle new uploads
            new_image_urls = []
            for f in request.FILES.getlist('store_images[]'):
                if not f:
                    continue
                file_extension = os.path.splitext(f.name)[1].lower()
                if file_extension not in IMAGE_EXTENSIONS:
                    continue

                unique_timestamp = now().strftime('%Y%m%d%H%M%S')
                file_name = f"{unique_timestamp}_{f.name}"
                saved_path = default_storage.save(file_name, f)
                full_media_url = f"{settings.MEDIA_URL}{saved_path}"
                new_image_urls.append(full_media_url)


            # Combine old + new
            updated_store.store_image_urls = existing_urls + new_image_urls
            updated_store.updated_by = get_object_or_404(UserModel, id=1)  # Replace with logged-in user
            updated_store.save()

            messages.success(request, "Store updated successfully!")
            return redirect('manage_Store_list')
        else:
            store_list = StoreModel.objects.all()
            messages.error(request, "Please correct the errors below.")
            return render(request, "admin/manage_store.html", {"form": form, "store_list": store_list})



class ToggleStoreStatus(View):
    def post(self, request, store_id):
        store = get_object_or_404(StoreModel, id=store_id)
        store.is_active = not store.is_active
        store.save()
        return redirect('manage_Store_list') 
    


# store category view

class ManageStoreCategoryView(View):
    def get(self,request):
        form = StoreCategoryForm()
        store_category=StoreCategoryModel.objects.all() 
        return render(request, "admin/manage_store_category.html", {"form": form, "store_category": store_category})   


class ManageCreateStoreCategoryView(View):
    def post(self, request, *args, **kwargs):
        form = StoreCategoryForm(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data['name']
            
            # Check if category already exists
            if StoreCategoryModel.objects.filter(name=category_name).exists():
                messages.error(request, "Category with this name already exists.")
                return render(request, "admin/manage_store_category.html", {"form": form})

            category = form.save(commit=False)
            user_instance = get_object_or_404(UserModel, id=1) 
            category.created_by = user_instance
            category.updated_by = user_instance
            category.save()

            messages.success(request, "Store category created successfully!")
            return redirect('manage_Store_category_list')  
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "admin/manage_store_category.html", {"form": form})
        


class ManageDeleteStoreCategoryView(View):
    def get(self, request, category_id, *args, **kwargs):
        category = get_object_or_404(StoreCategoryModel, id=category_id)
        category.delete()
        messages.success(request, "Store category deleted successfully!")
        return redirect("manage_Store_category_list")  # Re


class ToggleStoreCategoryStatus(View):
    def post(self, request, category_id):
        category = get_object_or_404(StoreCategoryModel, id=category_id)
        category.is_active = not category.is_active
        category.save()
        return redirect('manage_Store_category_list') 

class ManageCategoryUpdateStoreView(View):
    def post(self, request, pk):
        store = get_object_or_404(StoreCategoryModel, pk=pk)
        form = StoreCategoryForm(request.POST, instance=store)

        if form.is_valid():
            form.save()
            messages.success(request, "Store updated successfully!")
            return redirect('manage_Store_category_list')  # Ensure the URL name is correct
        else:
            messages.error(request, "Please correct the errors below.")
            
            # Ensure form errors are passed back to the template
            store_category_list = StoreCategoryModel.objects.all()
            return render(request, "admin/manage_store_category.html", {
                "form": form,
                "store_list": store_category_list,
                "store": store,  # Ensure the store object is passed
            })        