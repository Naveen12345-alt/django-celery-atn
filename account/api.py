from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializer import RegisterSerializer, UpdateSerializer, UserSerializer
from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend

# Register API
class RegisterApi(generics.GenericAPIView):
    permission_classes = []
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "message": "User Created Successfully.  Now perform Login to get your token",
            }
        )


class UpdateUserApi(generics.RetrieveUpdateAPIView):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UpdateSerializer


class RetrieveUserApi(generics.ListAPIView):
    permission_classes = ()
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        "username",
    ]
    # http://127.0.0.1:8000/account/api/retreive?username=alhaleel
