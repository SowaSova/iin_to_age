from rest_framework import viewsets

from .models import Person
from .serializers import PersonaSerializer


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonaSerializer
    lookup_field = "iin"
    