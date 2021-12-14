
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework import authentication
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authentication import SessionAuthentication


class MyAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # Get the email, username and password
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        if not username or not password or not email:
            raise exceptions.AuthenticationFailed(_('No credentials provided.'))

        credentials = {
            get_user_model().USERNAME_FIELD: username,
            'email': email,
            'password': password
        }

        user = authenticate(**credentials)

        if user is None:
            raise exceptions.AuthenticationFailed(_('Invalid username/password/email.'))

        if not user.is_email_active:
            raise exceptions.AuthenticationFailed(_('User inactive or deleted.'))

        return (user, None)  # authentication successful


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializers(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK, "Token": token.key})