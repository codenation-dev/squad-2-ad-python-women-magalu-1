from rest_framework import generics

from ..models import Error, User
from .serializers import ErrorSerializer, UserSerializer, ErrorSerializerInput

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


def is_not_null(args):
    return args != '' and args is not None

def ErrorFilter(request):
    queryset = Error.objects.filter(filed=False, deleted=False)
    environment = request.GET.get('environment')
    order_by = request.GET.get('order_by')
    search_for = request.GET.get('search_for')
    search = request.GET.get('search')

    if is_not_null(environment):
        queryset = queryset.filter(environment=environment)

    if is_not_null(order_by) and order_by != 'Ordenar por':
        queryset = queryset.order_by(order_by)

    if is_not_null(search_for) and is_not_null(search) and search_for != 'Filtro':
        queryset = queryset.filter(**{search_for+"__contains": search})

    return queryset


class ErrorDetailApiView(generics.RetrieveAPIView):
    """
        Busca os dados de um erro pela 'pk'.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer


class ErrorListCreateApiView(generics.ListCreateAPIView):
    """
        Busca todos os erros que não foram arquivados 
        e excluidos.

        Cria um novo cadastro do erro.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ErrorSerializer
    
    def get_queryset(self):
        queryset = ErrorFilter(self.request)
        return queryset

    def post(self, request):
        self.serializer_class = ErrorSerializerInput
        serializer = ErrorSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ErrorArchiveApiView(generics.UpdateAPIView):
    """
        Arquiva um erro pela pk
    """
    queryset = Error.objects.filter(filed=False, deleted=False)
    serializer_class = ErrorSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ErrorDeleteApiView(generics.UpdateAPIView):
    """
        Deleta um erro pela pk
    """
    queryset = Error.objects.filter(filed=False, deleted=False)
    serializer_class = ErrorSerializer


class UserCreateApiView(generics.CreateAPIView):
    """
        Cria um novo usuário.
    """
    permission_classes = []
    serializer_class = UserSerializer
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()
