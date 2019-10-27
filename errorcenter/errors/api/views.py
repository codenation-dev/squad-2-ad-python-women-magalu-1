from rest_framework import generics

from ..models import Error
from .serializers import ErrorSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import filters

class ErrorSearchFilter(filters.SearchFilter):
    """
        Seleciona o campo que está utilizado na busca de acordo com cada paramentro.

        Parâmetros (boolean):
            - level_only: busca a palavra apenas no campo level
            - desc_only: busca a palavra apenas no campo descrição
            - addr_only: busca a palavra apenas no campo origem/address
    """
    def get_search_fields(self, view, request):
        if request.query_params.get('level_only'):
            return ['level']
        elif request.query_params.get('desc_only'):
            return ['description']
        elif request.query_params.get('addr_only'):
            return ['address']
        return super(ErrorSearchFilter, self).get_search_fields(view, request)


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
    filter_backends = [OrderingFilter, DjangoFilterBackend, ErrorSearchFilter]
    filterset_fields = ['environment']
    ordering_fields = ['level', 'events']
    # search_field = ['level', 'description', 'address']
