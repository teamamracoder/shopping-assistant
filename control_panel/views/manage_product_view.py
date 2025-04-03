from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from ..models import ProductsModel, UserModel
from ..forms import ManageProductForm

class ManageProductListView(View):
    def get(self, request):
        products = ProductsModel.objects.all()
        form = ManageProductForm()
        return render(request, 'admin/manage_product.html', {"products": products, "form": form})


class ManageProductCreateView(View):
    """Handles product creation with GET and POST methods."""

    def get(self, request, *args, **kwargs):
        """Displays the product creation form."""
        form = ManageProductForm()
        products = ProductsModel.objects.all()
        return render(request, "admin/manage_product.html", {"form": form, "products": products})

    def post(self, request, *args, **kwargs):
        """Handles form submission and saves the product."""
        form = ManageProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)

            # Assign user if logged in, else set to None
            product.created_by = request.user if request.user.is_authenticated else None
            product.updated_by = request.user if request.user.is_authenticated else None
            product.save()

            messages.success(request, "Product created successfully!")
            return redirect('manage_product_list')  # Redirect to product list page
        
        else:
            messages.error(request, "Please correct the errors below.")
            products = ProductsModel.objects.all()
            return render(request, "admin/manage_product.html", {"form": form, "products": products})


class ManageProductEditView(View):
    """Handles updating an existing product."""

    def get(self, request, pk):
        """Displays the update form with existing product details."""
        product = get_object_or_404(ProductsModel, pk=pk)
        form = ManageProductForm(instance=product)
        products = ProductsModel.objects.all()  # Load all products for listing
        
        return render(request, "admin/manage_product.html", {
            "form": form, 
            "products": products,
            "edit_mode": True,  # Used in template to differentiate between create & update
            "product": product  # Pass the specific product being edited
        })

    def post(self, request, pk):
        """Handles form submission and updates the product."""
        product = get_object_or_404(ProductsModel, pk=pk)
        form = ManageProductForm(request.POST, request.FILES, instance=product)

        if form.is_valid():
            updated_product = form.save(commit=False)

            # Assign updated_by only if user is authenticated
            if request.user.is_authenticated:
                updated_product.updated_by = request.user

            updated_product.save()

            messages.success(request, "Product updated successfully!")
            return redirect('manage_product_list')  # Ensure this URL exists
        
        else:
            messages.error(request, "Please correct the errors below.")
            products = ProductsModel.objects.all()
            return render(request, "admin/manage_product.html", {
                "form": form, 
                "products": products,
                "edit_mode": True,
                "product": product
            })
        
class ManageProductDeleteView(View):
    """Handles product deletion."""

    def post(self, request, pk, *args, **kwargs):
        """Deletes a product and redirects to the product list."""
        product = get_object_or_404(ProductsModel, pk=pk)
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect("manage_product_list")  # Ensure this is the correct URL name