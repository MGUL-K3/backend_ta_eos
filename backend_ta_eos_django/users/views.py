from django.contrib.auth import authenticate, login, logout
from rest_framework import generics, status, views
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        answer = self.create(self.request, *args, **kwargs)

        if answer.status_code == status.HTTP_201_CREATED:
            email = self.request.data.get(
                "email",
            )
            password = self.request.data.get(
                "password",
            )
            user = authenticate(username=email, password=password)
            login(self.request, user)

        return answer

    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        request.user.update_last_visit()

        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class LoginView(views.APIView):
    permission_classes = [AllowAny]

    def post(self, *args, **kwargs):
        data = self.request.data

        email = data.get(
            "email",
        )

        password = data.get(
            "password",
        )
        user = authenticate(username=email, password=password)

        if user is None or not user.is_active:
            return Response(status=status.HTTP_404_NOT_FOUND)

        login(self.request, user)
        serializer = UserSerializer(user)
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_200_OK)
