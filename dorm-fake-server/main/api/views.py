from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Account
from .serializers import AccountSerializer, AuthSerializer
from django.db.models import Q


@api_view(['POST'])
@permission_classes((AllowAny,))
def auth_account(request):
    """Авторизация и выдача данных об акаунте."""
    try:
        body = AuthSerializer(data=request.data)
        if body.is_valid():
            account = Account.objects.get(
                Q(login=body.validated_data['login']), 
                Q(password=body.validated_data['password'])
            )
            serializer = AccountSerializer(account)
            return Response(serializer.data)
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    except Account.DoesNotExist:
        return Response(status=status.HTTP_409_CONFLICT)