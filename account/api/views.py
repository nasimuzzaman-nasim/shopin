from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from .serializers import AccountSerializer, Account


@api_view(['POST'])
def registration_view(request):

    serializer = AccountSerializer(data=request.data)
    data = {}

    if serializer.is_valid():
        account = serializer.save()
        data['response'] = 'User registered successfully!'
        data['username'] = account.username
        data['email'] = account.email
        data['token'] = Token.objects.get(user=account).key
        return Response(data, status=status.HTTP_201_CREATED)
    else:
        data = serializer.errors
    return Response(data, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_users_view(request):

    data = Account.objects.all()
    print(data)
    serializer = AccountSerializer(data, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

