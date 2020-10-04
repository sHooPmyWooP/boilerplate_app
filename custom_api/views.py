from custom_content.models import PlainText
from custom_api.serializers import PlainTextSerializer
from rest_framework import generics


class PlainTextList(generics.ListCreateAPIView):
    queryset = PlainText.objects.all()
    serializer_class = PlainTextSerializer


class PlainTextDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PlainText.objects.all()
    serializer_class = PlainTextSerializer
