from django.db import models
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="images", blank=True, null=True)
    audio = models.FileField(upload_to="audio", blank=True, null=True)
    video = models.FileField(upload_to="videos", blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, default=1)

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])

    def __str__(self):
        return self.title


# Create a model for comments that will be added later to the blog posts
class Comment(models.Model):
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE
    )  # Connects comment with the specific post it belongs to
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="comments"
    )  # Related name allows us to access all comments for a specific post
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="comments"
    )  # Related name is used to access the reverse relationship
    content = models.TextField()
    date_commented = models.DateTimeField(
        auto_now_add=True
    )  # Automatically adds the date and time of comment

    def __str__(self):
        return self.content


@receiver(post_delete, sender=Post)
def delete_post_media_files(sender, instance, **kwargs):
    # Delete associated media files when a Post object is deleted
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
    if instance.audio:
        if os.path.isfile(instance.audio.path):
            os.remove(instance.audio.path)
    if instance.video:
        if os.path.isfile(instance.video.path):
            os.remove(instance.video.path)
