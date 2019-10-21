from rest_framework import generics

from .models import Error
from .serializers import ErrorSerializer


class ErrorDetailApiView(generics.RetrieveAPIView):
    """
        Busca os dados de um erro pela 'pk'.
    """
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer


class ErrorListApiView(generics.ListAPIView):
    """
        Busca todos os erros que não foram arquivados 
        e excluidos.
    """
    queryset = Error.objects.filter(filed=False)
    serializer_class = ErrorSerializer
