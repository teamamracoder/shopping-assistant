from control_panel.models import UserModel

class UserService:
    def get_all_users(self):
        return UserModel.objects.all()

    def get_user_by_id(self,pk):
        try:
            return UserModel.objects.get(pk=pk)
        except UserModel.DoesNotExist:
            return None

    def create_user(self,validated_data):
        return UserModel.objects.create(**validated_data)

    def update_user(self,user, validated_data):
        user.name = validated_data.get('name', user.name)
        user.email = validated_data.get('email', user.email)
        user.phone = validated_data.get('phone', user.phone)
        user.save()
        return user

    def delete_user(self,user):
        user.delete()
