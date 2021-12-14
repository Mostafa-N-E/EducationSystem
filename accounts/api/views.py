
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import SessionAuthentication

from django.contrib.auth.hashers import check_password, make_password

from django.utils.timezone import now

from rest_auth.views import LoginView

class MyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Get the email, username and password
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not username or not password or not email:
            raise exceptions.AuthenticationFailed('No credentials provided.')

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'email': email,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid username/password/email.')

        if not user.is_email_active:
            raise exceptions.AuthenticationFailed('User inactive or deleted.')

        return (user, None)  # authentication successful


class LoginAPIView(LoginView):

    def login(self):
        # self.user = self.serializer.validated_data['user']
        #
        # if getattr(settings, 'REST_USE_JWT', False):
        #     self.token = jwt_encode(self.user)
        # else:
        #     self.token = create_token(self.token_model, self.user,
        #                               self.serializer)
        #
        # if getattr(settings, 'REST_SESSION_LOGIN', True):
        #     self.process_login()
        queryset = Person.objects.get(email=request.data['email'])
        if (check_password(request.data['password'], queryset.password)):
            token = Token.objects.get_or_create(user=user)

            obj = {
                "success": True,
                "data": token,
            }
            return Response(obj, status=status.HTTP_200_OK)
        obj = {
            "success": False,
            "message": "Incorrect Password!"
        }
        return Response(obj, status=status.HTTP_401_UNAUTHORIZED)

