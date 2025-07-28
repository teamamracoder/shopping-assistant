from django.views import View
from control_panel.models import UserModel

class ManageUserService:
    # Fetch and return all user records from the database
    def get_all_users(self):
        return UserModel.objects.all()
    
     # Create a new user with the provided data
    def manage_create_user(self,**user_data):
        user_data = UserModel.objects.create(
            first_name = user_data['first_name'],  # Set user's first name
            last_name  = user_data['last_name'],   # Set user's last name
            email      = user_data['email'],       # Set user's email address
            dob        = user_data['dob'],         # Set user's date of birth
            gender     = user_data['gender'],      # Set user's gender
            phone      = user_data['phone'],       # Set user's phone number
            address    = user_data['address'],     # Set user's address
            country    = user_data['country'],     # Set user's country
            location   = user_data['location'],    # Set user's location
            city       = user_data['city'],        # Set user's city
            district   = user_data['district'],    # Set user's district
            state      = user_data['state'],       # Set user's state
            pincode    = user_data['pincode'],     # Set user's postal/ZIP code
            roles      = user_data['roles'],       # Assign roles to the user
        )
        return user_data  # Return the newly created user object
    

    def manage_user_delete(self, user_id):
        # Retrieve the user instance by ID
        user = UserModel.objects.get(id=user_id)
            
        # Delete the user from the database
        user.delete()

# def get_user(user_id):
#     return get_object_or_404(User, id=user_id, is_active = True)

# # Work By Badhan
# def update_user(user_id,first_name,last_name,email,phone,gender,address,dob,country,bio,hobbies,relationship_status,profile_picture):
#     user = User.objects.get(id=user_id)
#     user.first_name = first_name
#     user.last_name = last_name
#     user.email = email
#     #user.phone = phone
#     user.gender = gender
#     user.address = address
#     user.dob = dob
#     user.country = country
#     user.bio=bio
#     user.hobbies=hobbies
#     user.relationship_status=relationship_status
#     if profile_picture:
#         user.profile_photo_url = profile_picture
#     user.updated_by = user
#     user.save()
#     #return user

# def filter_user(user_id):
#     return User.objects.filter(id=user_id)



# def calculate_age(date_of_birth):
#     """
#     Calculate age from date of birth.
#     """
#     from datetime import date
#     if date_of_birth:
#         today = date.today()
#         return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
#     return "N/A"



# def calculate_age(date_of_birth):
#     """
#     Calculate age from date of birth.
#     """
#     from datetime import date
#     if date_of_birth:
#         today = date.today()
#         return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
#     return "0"

#   # End by Badhan

# def delete_user(user):
#     user.delete()

# def get_user_by_email(email):
#     return User.objects.filter(email=email).first()

# def change_theme(user, ui_mode):
#     user.ui_mode = ui_mode
#     user.save()
#     return user


# def get_user_details(user_id):
#     return get_object_or_404(User, id=user_id)

# def get_user_name_and_img(user_id):
#     return User.objects.filter(id=user_id,is_active = True)

# def friends_count(user_id):
#     friends = Follower.objects.filter(user_id=user_id).select_related( 'following').count()
#     return friends

# def updateFCMToken(user_id,fcm_token):
#     user = User.objects.get(id=user_id)
#     user.fcm_token = fcm_token
#     user.save()

# def getFCMtoken(user_id):
#     return User.objects.filter(id=user_id).values_list('fcm_token', flat=True).first()


