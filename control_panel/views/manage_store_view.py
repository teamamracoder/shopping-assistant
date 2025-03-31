from django.shortcuts import render
from django.views import View
from ..forms .manage_store_form import *
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from ..models import UserModel,StoreModel
from services import *
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.urls import reverse

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
            user_instance = get_object_or_404(UserModel, id=1)  # Replace 1 with the appropriate user ID or logic
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