from datetime import timezone
from pyexpat.errors import messages
from django.views import View
from django.shortcuts import get_object_or_404, render, redirect
from ..models import ServiceBookingModel
from ..forms import ManageServiceBookingForm
from django.utils import timezone
from services import ServiceBookingModelService
service_book = ServiceBookingModelService()


#CREATE AND READ(ALL) VIEWS
class ManageServiceBookingCreateView(View):
    def get(self, request):
        service_booking = service_book.get_all_bookings()
        form = ManageServiceBookingForm()
        return render(request, 'admin/manage_service_booking_model.html', {
            'form': form,
            'service_bookings': service_booking  # <-- pass the data to HTML
        })

    def post(self, request):
        form = ManageServiceBookingForm(request.POST)
        if form.is_valid():
            booking_data = form.cleaned_data
            booking_data['created_at'] = timezone.now()
            booking_data['updated_at'] = timezone.now()
            booking_data['created_by'] = request.user if request.user.is_authenticated else None
            booking_data['updated_by'] = request.user if request.user.is_authenticated else None
            service_book.create_booking(booking_data)
            return redirect('manage_service_booking_create')
        
        # Form is invalid
        service_bookings = service_book.get_all_bookings()
        return render(request, 'admin/manage_service_booking_model.html', {
            'form': form,
            'service_bookings': service_bookings,
            'error': 'Please correct the errors below.'
        })        

#UPDATE VIEW
class ManageServiceBookingUpdateView(View):
    def post(self, request, pk):
        booking = service_book.get_booking_by_id(pk)
        form = ManageServiceBookingForm(request.POST, instance=booking)
        if form.is_valid():
            updated_data = form.cleaned_data
            updated_data['updated_at'] = timezone.now()
            updated_data['updated_by'] = request.user if request.user.is_authenticated else None
            service_book.update_booking(booking, updated_data)
            # Redirect back after update
            return redirect('manage_service_booking_create')

        # If form is invalid
        messages.error(request, "Please correct the errors below.")
        return render(request, 'admin/manage_service_booking_model.html', {
            'form': form,
            'is_update': True,
            'booking_id': pk
        })

#DELETE VIEW
class ManageServiceBookingDeleteView(View):
    def post(self, request, pk):
        booking = service_book.get_booking_by_id(pk)
        service_book.delete_booking(booking)
        return redirect('manage_service_booking_create')  # Update with correct view name

#TOGGLE VIEW
class ManageToggleServiceBookingActiveView(View):
    def post(self, request, pk):
        booking = service_book.get_booking_by_id(pk)
        service_book.toggle_active_status(booking)
        return redirect('manage_service_booking_create')  # Replace with actual view name