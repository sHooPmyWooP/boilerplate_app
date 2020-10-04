from rest_framework import serializers
from custom_content.models import PlainText


class PlainTextSerializer(serializers.ModelSerializer):
    """Serializer, that acts as an example for the PlainText class defined in the 'custom_content' app."""

    class Meta:
        model = PlainText
        fields = ["created_at", "updated_at", "plain_text"]
