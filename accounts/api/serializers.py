from rest_framework import serializers
from persons.models import User

# from .views.MyAuthentication import authenticate
#
# class LoginSerializers(serializers.Serializer):
#     username = serializers.CharField(max_length=255)
#     email = serializers.EmailField(max_length=255)
#     password = serializers.CharField(
#         label=_("Password"),
#         style={'input_type': 'password'},
#         trim_whitespace=False,
#         max_length=128,
#         write_only=True
#     )
#
#     def validate(self, data):
#         username = data.get('username')
#         email = data.get('email')
#         password = data.get('password')
#
#         if username and password and email:
#             user = authenticate(request=self.context.get('request'),
#                                 username=username, password=password, email=email)
#             if not user:
#                 msg = _('Unable to log in with provided credentials.')
#                 raise serializers.ValidationError(msg, code='authorization')
#         else:
#             msg = _('Must include "username" and "password".')
#             raise serializers.ValidationError(msg, code='authorization')
#
#         data['user'] = user
#         return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'