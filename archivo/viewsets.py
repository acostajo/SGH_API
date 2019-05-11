from rest_framework import viewsets
from .models import Archivo
from .serializers import ArchivoSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.response import Response # from viewsets doc
from rest_framework import permissions, status
from rest_framework.parsers import MultiPartParser, FormParser
class ArchivoViewSet(viewsets.ModelViewSet):
    queryset = Archivo.objects.all()
    serializer_class = ArchivoSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ("archivo_id",)
    permission_classes = (permissions.AllowAny,) # we assume that we have a session user
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        serializer = ArchivoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            for k, v in kwargs.items():
                for id in v.split(','):
                    obj = get_object_or_404(Archivo, pk=int(id))
                    self.perform_destroy(obj)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)