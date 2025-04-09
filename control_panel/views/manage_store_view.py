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


class ManageStoreView(View):
    def get(self, request):
        form = ManageStoreForm()
        store_list = StoreModel.objects.all()
        # Split email strings into lists
        for store in store_list:
            if isinstance(store.email, str):
                store.email = store.email.split(',')
        return render(request, "admin/manage_store.html", {"form": form, "store_list": store_list})


class ManageCreateStore(View):
    def post(self, request, *args, **kwargs):
        form = ManageStoreForm(request.POST)
        if form.is_valid():
            store = form.save(commit=False)
            # Retrieve the UserModel instance for the logged-in user
            user_instance = get_object_or_404(UserModel, id=11)  # Replace 1 with the appropriate user ID or logic
            store.owner = user_instance
            store.created_by = user_instance
            store.updated_by = user_instance
            store.save()
            messages.success(request, "Store created successfully!")
            return redirect('manage_Store_list')  # Ensure 'manage_store_list' is the correct URL name
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "admin/manage_store.html", {"form": form})
        

class ManageUpdateStoreView(View):
    def post(self, request, pk):
        store = get_object_or_404(StoreModel, pk=pk)
        form = ManageStoreForm(request.POST, instance=store)
        if form.is_valid():
            form.save()
            messages.success(request, "Store updated successfully!")
            return redirect('manage_Store_list')  # Ensure this is the correct URL name
        else:
            store_list=StoreModel.objects.all()
            for store in store_list:
                if isinstance(store.email, str):
                    store.email = store.email.split(',')
                if isinstance(store.contact_no, str):
                    store.contact_no = store.contact_no.split(',')
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
            user_instance = get_object_or_404(UserModel, id=11) 
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


# class ManageCategoryUpdateStoreView(View):
#     def post(self, request, pk):
#         store = get_object_or_404(StoreCategoryModel, pk=pk)
#         form = StoreCategoryForm(request.POST, instance=store)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Store updated successfully!")
#             return redirect('manage_Store_category_list')  # Ensure this is the correct URL name
#         else:
#             store_category_list=StoreCategoryModel.objects.all()
           
#             messages.error(request, "Please correct the errors below.")
#             return render(request, "admin/manage_store_category.html", {"form": form, "store_list": store_category_list})
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