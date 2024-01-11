from rest_framework import viewsets, filters
from .serializers import ImageSerializer
from .models import Images


# ViewSet for our UploadedImage Model
# Gets all images from database and serializes them using UploadedImageSerializer
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)