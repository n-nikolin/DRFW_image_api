from django.conf import settings
from django.db import models
import uuid

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)

def scramble_uploaded_filename(instance, filename):
    """
    Scramble / uglify the filename of the uploaded file, but keep the files extension (e.g., .jpg or .png)
    :param instance:
    :param filename:
    :return:
    """
    extension = filename.split(".")[-1]
    return "{}.{}".format(uuid.uuid4(), extension)

class Images(models.Model):
    """
    {
        id: int,
        image_url: string,
        owner: foreign_key,
        upload_date: datetime,
        title: charfield,
        description: textfield
    }
    """
    image_url = models.ImageField(max_length=None, null=False, upload_to=user_directory_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        # "user_api_appuser.AppUser", related_name="user_images", on_delete=models.CASCADE
        settings.AUTH_USER_MODEL, related_name="user_images", on_delete=models.CASCADE
    )
