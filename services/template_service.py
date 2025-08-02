import os
from django.conf import settings
from django.shortcuts import get_object_or_404
from control_panel.models import TemplateModel

class TemplateService:

    @staticmethod
    def list_templates():
        return TemplateModel.objects.all()

    @staticmethod
    def create_template(form, user, files):
        template = form.save(commit=False)

        if user and user.is_authenticated:
            template.created_by = user
            template.updated_by = user

        image_urls = []
        for f in files.getlist('template_images'):
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
        return template
    
    @staticmethod
    def update_template(form, user, files=None):
        template = form.save(commit=False)

        if user and user.is_authenticated:
            template.updated_by = user

        # Handle optional new images
        if files and files.getlist('template_images'):
            image_urls = []
            for f in files.getlist('template_images'):
                save_dir = os.path.join(settings.STATICFILES_DIRS[0], 'img/template')
                os.makedirs(save_dir, exist_ok=True)

                file_path = os.path.join(save_dir, f.name)
                with open(file_path, 'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)

                relative_url = os.path.join('img/template', f.name)
                image_urls.append(relative_url)

            template.image_urls = image_urls  # Replace old URLs

        template.save()
        return template


    @staticmethod
    def delete_template(pk):
        template = get_object_or_404(TemplateModel, pk=pk)
        template.delete()
        return True

    @staticmethod
    def toggle_active_status(pk):
        template = get_object_or_404(TemplateModel, pk=pk)
        template.is_active = not template.is_active
        template.save()
        return template
