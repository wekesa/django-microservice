from rest_framework import viewsets, routers,  serializers
from rest_framework.response import Response
from .models import Entry


class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry


class EntryViewSet(viewsets.ModelViewSet):
    model = Entry
    serializer_class = EntrySerializer


router = routers.DefaultRouter()
router.register('entry', EntryViewSet)
