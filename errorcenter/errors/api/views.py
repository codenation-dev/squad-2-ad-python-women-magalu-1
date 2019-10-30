from rest_framework import generics

from ..models import Error
from .serializers import ErrorSerializer


def is_not_null(args):
    return args != '' and args is not None

def ErrorFilter(request):
    queryset = Error.objects.filter(filed=False)
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
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer


class ErrorListCreateApiView(generics.ListCreateAPIView):
    """
        Busca todos os erros que não foram arquivados 
        e excluidos.

        Cria um novo cadastro do erro.
    """
    serializer_class = ErrorSerializer
    def get_queryset(self):
        queryset = ErrorFilter(self.request)
        return queryset
