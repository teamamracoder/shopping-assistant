from django.shortcuts import render
from django.views import View
from ..forms import ProductSubCategoryCreateForm

class ManageProductSubCategoryListView(View):
    def get(self, request):
        form = ProductSubCategoryCreateForm()
        return render(request, "admin/manage_product_sub_category.html",{"form": form})

# class ManageProductSubCategoryCreateView(View):
#     def get(self, request):
#         return render(request, "admin/manage_product_sub_category.html")

