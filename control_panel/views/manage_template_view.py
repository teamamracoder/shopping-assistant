from django.views import View
from django.views.generic import UpdateView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.models import AnonymousUser
from control_panel.models import TemplateModel
from control_panel.forms.manage_template_form import ManageTemplateForm
from services.template_service import TemplateService

template_service =TemplateService()

## List ##
class ManageTemplateListView(View):
    def get(self, request):
        templates = template_service.list_templates()  # ✅ Service call
        form = ManageTemplateForm()
        return render(request, 'temp/manage_template_list.html', {
            "templates": templates,
            "form": form
        })


## Create ##
class ManageTemplateCreateView(View):
    def get(self, request):
        form = ManageTemplateForm()
        templates = TemplateModel.objects.all()
        return render(request, "temp/manage_template_create.html", {
            "form": form,
            "templates": templates
        })

    def post(self, request):
        form = ManageTemplateForm(request.POST, request.FILES)
        if form.is_valid():
            template_service.create_template(form, request.user, request.FILES)
            messages.success(request, "Email Template added successfully!")
            return redirect("manage_template_list")

        messages.error(request, "Please correct the errors below.")
        templates = TemplateModel.objects.all()
        return render(request, "temp/manage_template_create.html", {
            "form": form,
            "templates": templates
        })


## Update ##
class ManageTemplateEditView(UpdateView):
    model = TemplateModel
    form_class = ManageTemplateForm
    template_name = 'temp/manage_template_update.html'
    success_url = reverse_lazy('manage_template_list')

    def form_valid(self, form):
        # ✅ Use service method to update template
        template_service.update_template(form, self.request.user, self.request.FILES)
        messages.success(self.request, "Template updated successfully.")
        return super().form_valid(form)


## Delete ##
class ManageTemplateDeleteView(View):
    def post(self, request, pk):
        template_service.delete_template(pk)
        messages.success(request, "Template deleted successfully!")
        return redirect("manage_template_list")

 
## Toggle Active/Inactive ##
class ManageToggletemplatesActiveView(View):
    def post(self, request, pk):
        template = template_service.toggle_active_status(pk)
        status = "activated" if template.is_active else "deactivated"
        messages.success(request, f"Template '{template.subject}' has been {status}.")
        return redirect("manage_template_list")