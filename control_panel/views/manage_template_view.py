import json
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from control_panel.models import TemplateModel
from control_panel.forms.manage_template_form import ManageTemplateForm
import os
from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from django.views.generic import UpdateView
from django.urls import reverse_lazy


#List
class ManageTemplateListView(View):
    def get(self, request):
        templates = TemplateModel.objects.all()
        form = ManageTemplateForm()
        return render(request, 'temp/manage_template_list.html', {"templates": templates, "form": form})
    

#Create
class ManageTemplateCreateView(View):
    """Handles template creation with image support."""

    def get(self, request): 
        form = ManageTemplateForm()
        templates = TemplateModel.objects.all()
        return render(request, "temp/manage_template_create.html", {"form": form, "templates": templates})

    def post(self, request):
        form = ManageTemplateForm(request.POST, request.FILES)  # Fix: include request.FILES

        if form.is_valid():
            template = form.save(commit=False)

            if not isinstance(request.user, AnonymousUser):
                template.created_by = request.user
                template.updated_by = request.user

            image_urls = []
            for f in request.FILES.getlist('template_images'):
                save_dir = os.path.join(settings.STATICFILES_DIRS[0], 'img/template')
                os.makedirs(save_dir, exist_ok=True)

                file_path = os.path.join(save_dir, f.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

                relative_url = os.path.join('img/template', f.name)
                image_urls.append(relative_url)

            template.image_urls = image_urls
            template.save()

            messages.success(request, "Template created successfully!")
            return redirect("manage_template_list")

        messages.error(request, "Please correct the errors below.")
        templates = TemplateModel.objects.all()
        return render(request, "temp/manage_template_create.html", {
            "form": form,
            "templates": templates
        })

    

# Update
class ManageTemplateEditView(UpdateView):
    model = TemplateModel
    form_class = ManageTemplateForm
    template_name = 'temp/manage_template_update.html'  # 👈 Add this line
    success_url = reverse_lazy('manage_template_list')
    def form_valid(self, form):
        return super().form_valid(form)



# Delete
class ManageTemplateDeleteView(View):
    """Handles template deletion."""

    def post(self, request, pk, *args, **kwargs):
        """Deletes a template and redirects to the template list."""
        template = get_object_or_404(TemplateModel, pk=pk)
        template.delete()
        messages.success(request, "template deleted successfully!")
        return redirect("manage_template_list")  # Ensure this is the correct URL name


# Toggle Button
class ManageToggletemplatesActiveView(View):
    def post(self, request, pk, *args, **kwargs):
        template = get_object_or_404(TemplateModel, pk=pk)
        template.is_active = not template.is_active
        template.save()

        status = "activated" if template.is_active else "deactivated"
        messages.success(request, f"Template '{template.subject}' has been {status}.")
        
        return redirect('manage_template_list')