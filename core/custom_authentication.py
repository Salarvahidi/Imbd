from datetime import timedelta

from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions

from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class CustomAuthentication(TokenAuthentication):
    def authenticate(self, request):
        if "token" in request.query_params and "HTTP_AUTHORIZATION" not in request.META:
            auth_token = request.query_params.get("token")
            token = self.authenticate_credentials(auth_token)
        else:
            token = super().authenticate(request)

        if token is None:
            return None

        user, token = token

        if token.created < (timezone.now() - timedelta(hours=3)):
            token.delete()
            msg = _("Invalid token.")
            raise exceptions.AuthenticationFailed(msg)

        token.created = timezone.now()
        token.save()

        return user, token
