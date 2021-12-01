from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
@api_view(("POST",))
def logout_view(request):
    """Blacklist the refresh token: extract token from the header
    during logout request user and refresh token is provided"""
    Refresh_token = request.data["refresh"]
    Access_token = request.data["access"]

    token = RefreshToken(Refresh_token)
    token.blacklist()
    return Response("Successful Logout", status=status.HTTP_200_OK)
