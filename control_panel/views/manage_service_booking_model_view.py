from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from django.utils import timezone
from services import ServiceBookingModelService
from ..forms import ManageServiceBookingForm
from utils.common_utils import get_user_id

service_book = ServiceBookingModelService()
from decorators.validator import role_required
from constants import Role

# # CREATE + LIST VIEW
# class ManageServiceBookingCreateView(View):
#     def get(self, request):
#         bookings = service_book.get_all_bookings()
#         form = ManageServiceBookingForm()
#         return render(request, 'admin/manage_service_booking_model.html', {
#             'form': form,
#             'service_bookings': bookings
#         })

#     def post(self, request):
#         form = ManageServiceBookingForm(request.POST)
#         if form.is_valid():
#             booking_data = form.cleaned_data
#             booking_data.update({
#                 'created_at': timezone.now(),
#                 'updated_at': timezone.now(),
#                 'created_by': request.user if request.user.is_authenticated else None,
#                 'updated_by': request.user if request.user.is_authenticated else None,
#             })
#             service_book.create_booking(booking_data)
#             messages.success(request, "Service Booking added successfully!")
#             return redirect('manage_service_booking_create')
#         else:
#             messages.error(request, "Error: Please correct the form errors.")
#             bookings = service_book.get_all_bookings()
#             return render(request, 'admin/manage_service_booking_model.html', {
#                 'form': form,
#                 'service_bookings': bookings
#             })

class ManageServiceBookingCreateView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def get(self, request):
        bookings = service_book.get_all_bookings()
        form = ManageServiceBookingForm()
        return render(request, 'admin/manage_service_booking_model.html', {
            'form': form,
            'service_bookings': bookings
        })

    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request):
        form = ManageServiceBookingForm(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)

            # Set created_by / updated_by using get_user_id
            user_id = get_user_id(request)
            booking_instance.created_by = user_id
            booking_instance.updated_by = user_id
            booking_instance.created_at = timezone.now()
            booking_instance.updated_at = timezone.now()

            try:
                booking_instance.save()
                messages.success(request, "Service Booking added successfully!")
                return redirect('manage_service_booking_create')
            except Exception as e:
                messages.error(request, f"Error saving booking: {str(e)}")
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        bookings = service_book.get_all_bookings()
        return render(request, 'admin/manage_service_booking_model.html', {
            'form': form,
            'service_bookings': bookings
        })

# UPDATE
# class ManageServiceBookingUpdateView(View):
#     def post(self, request, pk):
#         booking = service_book.get_booking_by_id(pk)
#         form = ManageServiceBookingForm(request.POST, instance=booking)
#         if form.is_valid():
#             updated_data = form.cleaned_data
#             updated_data.update({
#                 'updated_at': timezone.now(),
#                 'updated_by': request.user if request.user.is_authenticated else None
#             })
#             service_book.update_booking(booking, updated_data)
#             messages.success(request, "Service Booking updated successfully!")
#         else:
#             messages.error(request, "Error: Invalid form submission.")
#         return redirect('manage_service_booking_create')

class ManageServiceBookingUpdateView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk):
        booking_instance = service_book.get_booking_by_id(pk)
        if not booking_instance:
            messages.error(request, "Booking not found.")
            return redirect('manage_service_booking_create')

        form = ManageServiceBookingForm(request.POST, instance=booking_instance)
        if form.is_valid():
            booking_instance = form.save(commit=False)

            # Update updated_by using get_user_id
            booking_instance.updated_by = get_user_id(request)
            booking_instance.updated_at = timezone.now()

            try:
                booking_instance.save()
                messages.success(request, "Service Booking updated successfully!")
            except Exception as e:
                messages.error(request, f"Error updating booking: {str(e)}")
        else:
            for field, error in form.errors.items():
                messages.error(request, f"{field.capitalize()}: {error}")

        return redirect('manage_service_booking_create')


# DELETE
class ManageServiceBookingDeleteView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk):
        booking = service_book.get_booking_by_id(pk)
        if booking:
            service_book.delete_booking(booking)
            messages.success(request, "Service Booking deleted successfully!")
        else:
            messages.error(request, "Error: Booking not found.")
        return redirect('manage_service_booking_create')


# TOGGLE ACTIVE STATUS
class ManageToggleServiceBookingActiveView(View):
    @role_required(Role.ADMIN.value, Role.SERVICE_PROVIDER.value, Role.SELLER.value)
    def post(self, request, pk):
        booking = service_book.get_booking_by_id(pk)
        if booking:
            updated_booking = service_book.toggle_active_status(booking)
            status = "activated" if updated_booking.is_active else "deactivated"
            messages.success(request, f"Service Booking has been {status} successfully!")
        else:
            messages.error(request, "Error: Booking not found.")
        return redirect('manage_service_booking_create')
