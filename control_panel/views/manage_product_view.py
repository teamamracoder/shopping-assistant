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
            product.save()

            messages.success(request, "Product created successfully!")
            return redirect("manage_product_list")
        
        messages.error(request, "Please correct the errors below.")
        return render(request, "admin/manage_product.html", {"form": form})


#Update
class ManageProductEditView(UpdateView):
    model = ProductsModel
    form_class = ManageProductForm
    success_url = reverse_lazy('manage_product_list')

    def form_valid(self, form):
        return super().form_valid(form)

    
#Delete     
class ManageProductDeleteView(View):
    """Handles product deletion."""

    def post(self, request, pk, *args, **kwargs):
        """Deletes a product and redirects to the product list."""
        product = get_object_or_404(ProductsModel, pk=pk)
        product.delete()
        messages.success(request, "Product deleted successfully!")
        return redirect("manage_product_list")  # Ensure this is the correct URL name