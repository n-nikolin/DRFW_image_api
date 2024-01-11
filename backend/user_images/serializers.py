from rest_framework import serializers
from .models import Images


# Serializer for UploadedImage Model
# serializes pk and image
class ImageSerializer(serializers.ModelSerializer):
    """
    Serializer for the UPloadedImage Model
    Provides the pk, image, thumbnail, title and description
    """
    owner = serializers.ReadOnlyField(source='user.user_id')
    owner_id = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Images
        fields = ('image_url', 'title', 'description', 'owner', 'owner_id')