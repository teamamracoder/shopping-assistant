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
