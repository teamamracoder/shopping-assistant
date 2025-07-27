from control_panel.models import UserModel
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from constants.enums import Role

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
        except Exception as e:
            raise ValidationError(f"Error creating user: {str(e)}")
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
            for attr, value in validated_data.items():
                setattr(user, attr, value)
            # Save the updated user
            user.save()
            return user
        except Exception as e:
            raise ValidationError(f"Error updating user: {str(e)}")
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
    
    def user_exists(self, email):
        """
        Check if a user exists by email.
        :param email: Email address to check.
        :return: True if user exists, False otherwise.
        """
        return UserModel.objects.filter(email=email).exists()
    
    def get_user_by_email(self, email):
        """
        Fetch a user by their email address.
        :param email: Email address of the user.
        :return: UserModel instance if found, None otherwise.
        """
        try:
            return UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            return None
        
    def get_my_customers(user):
        """
        Fetch customers associated with the Business Partner .
        :param user: Business Partner UserModel instance.
        :return: Queryset of UserModel instances representing customers.
        """

        return UserModel.objects.filter(is_seller=False, is_service_provider=False).exclude(roles__contains=[Role.ADMIN.value])
        
user_service = UserService()