from datetime import timezone
from pyexpat.errors import messages
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from ..models import ServiceBookingModel
from ..forms import ManageServiceBookingForm
from django.utils import timezone

# JUST ADD PREFIX Manage in clss name

#CREATE AND READ(ALL) VIEWS
class ManageServiceBookingCreateView(View):
    def get(self, request):
        service_booking = ServiceBookingModel.objects.all()
        form = ManageServiceBookingForm()
        return render(request, 'admin/manage_service_booking_model.html', {
            'form': form,
            'service_bookings': service_booking  # <-- pass the data to HTML
        })

    def post(self, request):
        form = ManageServiceBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)

            # Add any extra logic here (e.g., who is creating it)
            booking.created_at = timezone.now()
            booking.updated_at = timezone.now()
            booking.created_by = request.user if request.user.is_authenticated else None
            booking.updated_by = request.user if request.user.is_authenticated else None
            booking.save()
            return redirect('manage_service_booking_create')  # Make sure this URL name is defined in urls.py
        else:
            service_booking = ServiceBookingModel.objects.all()

            return render(request, 'admin/manage_service_booking_model.html', {
                'form': form,
                'service_bookings': service_booking,
                'error': 'Please correct the errors below.'
            })
        

#UPDATE VIEW
class ManageServiceBookingUpdateView(View):
    def post(self, request, pk):
        booking = get_object_or_404(ServiceBookingModel, pk=pk)
        print(f"Requrst for update id ========= {pk}")
        form = ManageServiceBookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            # messages.success(request, "Service booking updated successfully.")
            return redirect('manage_service_booking_create')
        else:
            messages.error(request, "Please correct the errors below.")            
            return render(request, 'admin/manage_service_booking_model.html', {
                'form': form,
                'is_update': True,
                'booking_id': pk
            })


#DELETE VIEW
class ManageServiceBookingDeleteView(View):
    def post(self, request, pk):
        booking = get_object_or_404(ServiceBookingModel, pk=pk)
        booking.delete()
        # messages.success(request, "Service booking deleted successfully.")
        return redirect('manage_service_booking_create')  # Replace with your actual list view name
    

#TOGGLE VIEW
class ManageToggleServiceBookingActiveView(View):
    def post(self, request, pk):
        booking = get_object_or_404(ServiceBookingModel, pk=pk)
        booking.is_active = not booking.is_active
        booking.save()
        return redirect('manage_service_booking_create')  # Replace with your actual list view name
    
