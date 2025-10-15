import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from ..forms import ManageProductForm
from services.product_service import ProductModelService
from django.core.exceptions import ValidationError
from control_panel.models import ProductsModel  
from utils.common_utils import get_user_id

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
        print("[DEBUG] Current user:", get_user_id(request))

        form = ManageProductForm(request.POST, request.FILES)

        if form.is_valid():
            product_data = form.cleaned_data.copy()

            # Attach user info
            product_data['created_by'] = get_user_id(request)
            product_data['updated_by'] = get_user_id(request)

            # Initialize empty image_urls list
            product_data['image_urls'] = []

            try:
                # Create product without images first using service
                product = product_service.create_product(product_data)

                # Handle image upload (single or multiple)
                images = request.FILES.getlist('product_images')
                if images:
                    save_dir = os.path.join(settings.MEDIA_ROOT, 'img/product')
                    os.makedirs(save_dir, exist_ok=True)

                    for f in images:
                        save_path = os.path.join(save_dir, f.name)
                        with open(save_path, 'wb+') as destination:
                            for chunk in f.chunks():
                                destination.write(chunk)
                        relative_url = f'media/img/product/{f.name}'
                        product.image_urls.append(relative_url)

                    # Save product after adding images
                    product.save()

                messages.success(request, "Product added successfully!", extra_tags='product')
                return redirect("manage_product_list")

            except Exception as e:
                messages.error(request, f"Error: {str(e)}")
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
        print("[DEBUG] Current user:", get_user_id(request))        
        product = product_service.get_product_by_id(pk)
        if not product:
            messages.error(request, "Product not found.")
            return redirect("manage_product_list")

        form = ManageProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            updated_data = form.cleaned_data.copy()

            # if request.user.is_authenticated:
            updated_data['updated_by'] = get_user_id(request)

            # Keep existing images
            image_urls = product.image_urls if product.image_urls else []

            # Handle new image uploads
            new_images = request.FILES.getlist('product_images')
            if new_images:
                save_dir = os.path.join(settings.MEDIA_ROOT, 'img/product')
                os.makedirs(save_dir, exist_ok=True)

                for f in new_images:
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
                messages.success(request, "Product updated successfully!", extra_tags="product")
                return redirect("manage_product_list")
            except ValidationError as e:
                messages.error(request, str(e))
        else:
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
            messages.success(request, "Product deleted successfully!", extra_tags="product")
        except ValidationError as e:
            messages.error(request, str(e))

        return redirect("manage_product_list")


# Toggle Active/Inactive View
class ManageToggleProductActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        try:
            product = product_service.toggle_product_status(pk, updated_by=request.user)
            if product.is_active:
                messages.success(request, f"Product '{product.name}' has been activated successfully!", extra_tags="product")
            else:
                messages.success(request, f"Product '{product.name}' has been deactivated successfully!", extra_tags="product")
        except ValidationError as e:
            messages.error(request, str(e), extra_tags="product")

        return redirect("manage_product_list")

