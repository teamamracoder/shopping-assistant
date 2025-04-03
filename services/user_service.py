# from control_panel.models import UserModel

# class UserService:
#     def get_all_users(self):
#         return UserModel.objects.all()

#     def get_user_by_id(self, pk):
#         try:
#             return UserModel.objects.get(pk=pk)
#         except UserModel.DoesNotExist:
#             return None

#     def create_user(self, validated_data):
#         return UserModel.objects.create(**validated_data)

#     def update_user(self, user, validated_data):
#         user.first_name = validated_data.get('first_name', user.first_name)
#         user.last_name = validated_data.get('last_name', user.last_name)
#         user.email = validated_data.get('email', user.email)
#         user.phone = validated_data.get('phone', user.phone)
#         user.gender = validated_data.get('gender', user.gender)
#         user.dob = validated_data.get('dob', user.dob)
#         user.address = validated_data.get('address', user.address)
#         user.location = validated_data.get('location', user.location)
#         user.city = validated_data.get('city', user.city)
#         user.district = validated_data.get('district', user.district)
#         user.state = validated_data.get('state', user.state)
#         user.pincode = validated_data.get('pincode', user.pincode)
#         user.image_url = validated_data.get('image_url', user.image_url)
#         user.is_seller = validated_data.get('is_seller', user.is_seller)
#         user.is_service_provider = validated_data.get('is_service_provider', user.is_service_provider)
#         user.designation = validated_data.get('designation', user.designation)
#         user.bio = validated_data.get('bio', user.bio)
#         user.roles = validated_data.get('roles', user.roles)  # Handle ArrayField update properly

#         user.save()
#         return user

#     def delete_user(self, user):
#         user.delete()





from control_panel.models import UserModel
from django.core.exceptions import ValidationError
from django.db import IntegrityError

class UserService:
    
    def get_all_users(self):
        """
        Fetch all users from the database.
        :return: Queryset of all UserModel instances.
        """
        return UserModel.objects.all()

    def get_user_by_id(self, pk):
        """
        Fetch a user by their primary key (ID).
        :param pk: Primary key (ID) of the user.
        :return: UserModel instance if found, None otherwise.
        """
        try:
            return UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return None  # User not found.

    def create_user(self, validated_data):
        """
        Create a new user from validated data.
        :param validated_data: A dictionary of user data to create a new user.
        :return: Newly created UserModel instance.
        :raises IntegrityError: In case of database constraints (e.g., email already exists).
        """
        try:
            # Create and save a new user object
            return UserModel.objects.create(**validated_data)
        except IntegrityError:
            raise ValidationError("A user with this email already exists.")  # Handle unique constraint violations.

    def update_user(self, user, validated_data):
        """
        Update an existing user with new validated data.
        :param user: UserModel instance to be updated.
        :param validated_data: A dictionary of data to update the user with.
        :return: Updated UserModel instance.
        :raises ValidationError: If the updated data fails validation.
        """
        try:
            # Update fields based on the validated data provided
            user.first_name = validated_data.get('first_name', user.first_name)
            user.last_name = validated_data.get('last_name', user.last_name)
            user.gender = validated_data.get('gender', user.gender)
            user.dob = validated_data.get('dob', user.dob)
            user.email = validated_data.get('email', user.email)
            user.phone = validated_data.get('phone', user.phone)
            user.address = validated_data.get('address', user.address)
            user.city = validated_data.get('city', user.city)
            user.state = validated_data.get('state', user.state)
            user.pincode = validated_data.get('pincode', user.pincode)
            user.is_active = validated_data.get('is_active', user.is_active)
            user.bio = validated_data.get('bio', user.bio)

            # Save the updated user
            user.save()
            return user
        except IntegrityError:
            raise ValidationError("Email already exists, or another integrity issue occurred.") 

    def delete_user(self, user):
        """
        Delete a user.
        :param user: UserModel instance to be deleted.
        :return: None
        :raises ValidationError: If deletion fails.
        """
        try:
            user.delete()
        except Exception as e:
            raise ValidationError(f"Error deleting user: {str(e)}")
    
    def activate_user(self, user):
        """
        Activate a user.
        :param user: UserModel instance to be activated.
        :return: Activated UserModel instance.
        """
        user.is_active = True
        user.save()
        return user

    def deactivate_user(self, user):
        """
        Deactivate a user.
        :param user: UserModel instance to be deactivated.
        :return: Deactivated UserModel instance.
        """
        user.is_active = False
        user.save()
        return user
