from rest_framework import viewsets
from . import models
from . import serializers

class MemeViewsets(viewsets.ModelViewSet):
    queryset=models.Meme.objects.all()
    serializer_class=serializers.MemeSerializer