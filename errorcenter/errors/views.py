from rest_framework import generics

from .models import Error
from .serializers import ErrorSerializer


class ErrorDetailApiView(generics.RetrieveAPIView):
    queryset = Error.objects.all()
    serializer_class = ErrorSerializer
