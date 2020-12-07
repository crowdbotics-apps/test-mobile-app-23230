from rest_framework import authentication
from testapp.models import Vehicle
from .serializers import VehicleSerializer
from rest_framework import viewsets


class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Vehicle.objects.all()
