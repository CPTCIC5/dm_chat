from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CreateUserSerializer
from django.contrib.auth import authenticate,login


class RegisterAPI(APIView):
    def post(self, request, format=None):
        serializer= CreateUserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            if serializer.validated_data["password"] == serializer.validated_data["confirm_password"]:
                print('auth hua')
                serializer.validated_data.pop("confirm_password")
                serializer.save()
                authenticatee= authenticate(request,**serializer.validated_data)
                print(authenticatee)
                login(request,authenticatee)
                print('logged in')

                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class LoginAPI(APIView):
    pass