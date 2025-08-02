import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from ..forms import ManageProductForm
from services.product_service import ProductModelService
from django.core.exceptions import ValidationError

product_service = ProductModelService()

# List View
class ManageProductListView(View):
    def get(self, request):
        products = product_service.get_all_products()
        print(products)
        form = ManageProductForm()
        return render(request, 'admin/manage_product.html', {"products": products, "form": form})


# Create View
class ManageProductCreateView(View):
    def get(self, request): 
        form = ManageProductForm()
        products = product_service.get_all_products()
        return render(request, "admin/manage_product.html", {"form": form, "products": products})

    def post(self, request):
        form = ManageProductForm(request.POST)

        if form.is_valid():
            product_data = form.cleaned_data

            # Attach created_by and updated_by if user is authenticated
            if not isinstance(request.user, AnonymousUser):
                product_data['created_by'] = request.user
                product_data['updated_by'] = request.user

            # Handle file upload
            image_urls = []
            for f in request.FILES.getlist('product_images'):
                save_dir = os.path.join(settings.MEDIA_ROOT, 'img/product')
                os.makedirs(save_dir, exist_ok=True)
                save_path = os.path.join(save_dir, f.name)
                with open(save_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                relative_url = f'media/img/product/{f.name}'
                image_urls.append(relative_url)

            product_data['image_urls'] = image_urls

            try:
                product_service.create_product(product_data)
                messages.success(request, "Product added successfully!", extra_tags='product')
                return redirect("manage_product_list")
            except ValidationError as e:
                messages.error(request, str(e))
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        return render(request, "admin/manage_product.html", {
            "form": form,
            "products": product_service.get_all_products()
        })


# Edit View
class ManageProductEditView(View):
    def post(self, request, pk):
        product = product_service.get_product_by_id(pk)
        if not product:
            messages.error(request, "Product not found.")
            return redirect("manage_product_list")

        form = ManageProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            updated_data = form.cleaned_data

            # Handle image file upload if present
            image_urls = product.image_urls or []

            for f in request.FILES.getlist('product_images'):
                save_dir = os.path.join(settings.MEDIA_ROOT, 'img/product')
                os.makedirs(save_dir, exist_ok=True)
                save_path = os.path.join(save_dir, f.name)
                with open(save_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
                relative_url = f'media/img/product/{f.name}'
                image_urls.append(relative_url)

            updated_data['image_urls'] = image_urls

            # Attach updater info
            if not isinstance(request.user, AnonymousUser):
                updated_data['updated_by'] = request.user

            try:
                product_service.update_product(product, updated_data)
                messages.success(request, "Product updated successfully!")
                return redirect("manage_product_list")
            except ValidationError as e:
                messages.error(request, str(e))

        messages.error(request, "Please correct the errors below.")
        return render(request, "admin/manage_product.html", {
            "form": form,
            "products": product_service.get_all_products()
        })


# Delete View
class ManageProductDeleteView(View):
    def post(self, request, pk, *args, **kwargs):
        product = product_service.get_product_by_id(pk)
        if not product:
            messages.error(request, "Product not found.")
            return redirect("manage_product_list")

        try:
            product_service.delete_product(product)
            messages.success(request, "Product deleted successfully!")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_product_list")


# Toggle Active/Inactive View
class ManageToggleProductActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        try:
            product = product_service.toggle_product_status(pk, updated_by=request.user)
            status = "activated" if product.is_active else "deactivated"
            messages.success(request, f"Product '{product.name}' has been {status}.")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_product_list")
