import os
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from ..models import ProductsModel, UserModel
from ..forms import ManageProductForm
from django.contrib.auth.models import AnonymousUser
from django.urls import reverse_lazy
from django.views.generic import UpdateView


#List
class ManageProductListView(View):
    def get(self, request):
        products = ProductsModel.objects.all()
        form = ManageProductForm()
        return render(request, 'admin/manage_product.html', {"products": products, "form": form})


#Create
class ManageProductCreateView(View):
    """Handles product creation with proper debugging."""

    def get(self, request): 
        form = ManageProductForm()
        products = ProductsModel.objects.all()
        return render(request, "admin/manage_product.html", {"form": form, "products": products})

    def post(self, request):
        form = ManageProductForm(request.POST)

        if form.is_valid():
            product = form.save(commit=False)

            # Only assign user if they are authenticated
            if not isinstance(request.user, AnonymousUser):
                product.created_by = request.user
                product.updated_by = request.user

            # Handle multiple uploaded files manually
            image_urls = []
            for f in request.FILES.getlist('product_images'):
                save_path = os.path.join(settings.STATIC_ROOT, 'img/product', f.name)
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                with open(save_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

                relative_url = f'static/img/product/{f.name}'
                image_urls.append(relative_url)

            product.image_urls = image_urls
            product.save()

            messages.success(request, "Product created successfully!")
            return redirect("manage_product_list")
        
        messages.error(request, "Please correct the errors below.")
        return render(request, "admin/manage_product.html", {"form": form})


#Update
# class ManageProductEditView(UpdateView):
#     model = ProductsModel
#     form_class = ManageProductForm
#     success_url = reverse_lazy('manage_product_list')

#     def form_valid(self, form):
#         return super().form_valid(form)


class ManageProductEditView(View):
    def post(self, request, pk):
        product = get_object_or_404(ProductsModel, pk=pk)
        print("cgbfvhgvhv",product)
        form = ManageProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            updated_product = form.save(commit=False)

            # Check if new image is uploaded
            if 'product_images' in request.FILES:
                uploaded_file = request.FILES['product_images']
                save_path = os.path.join(settings.STATIC_ROOT, 'img/product', uploaded_file.name)
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                with open(save_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                relative_url = f'static/img/product/{uploaded_file.name}'
                updated_product.product_images = relative_url

            updated_product.save()
            messages.success(request, "product updated successfully!")
            return redirect('manage_product_list')
        else:
            product_list = ProductsModel.objects.all()
            messages.error(request, "Please correct the errors below.")
            return render(request, "admin/manage_product.html", {"form": form, "product_list": product_list})


    
# Delete     
class ManageProductDeleteView(View):
    """Handles product deletion."""

    def post(self, request, pk, *args, **kwargs):
        """Deletes a product and redirects to the product list."""
        product = get_object_or_404(ProductsModel, pk=pk)
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect("manage_product_list")  # Ensure this is the correct URL name
    
    
# Toggle Button
class ManageToggleProductActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        product = get_object_or_404(ProductsModel, pk=pk)
        product.is_active = not product.is_active
        product.save()

        status = "activated" if product.is_active else "deactivated"
        messages.success(request, f"Product '{product.name}' has been {status}.")
        
        return redirect('manage_product_list')