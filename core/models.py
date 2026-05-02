from django.db import models


class GalleryLook(models.Model):
    CATEGORY_CHOICES = [
        ('evening', 'איפור ערב | مكياج سهرة'),
        ('bridal', 'איפור כלה | مكياج عروس'),
    ]

    title = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title or self.get_category_display()


class GalleryMedia(models.Model):
    MEDIA_TYPE_CHOICES = [
        ('image', 'Image'),
        ('video', 'Video'),
    ]

    look = models.ForeignKey(
        GalleryLook,
        on_delete=models.CASCADE,
        related_name='media_items'
    )
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPE_CHOICES)
    image = models.ImageField(upload_to='gallery/images/', blank=True, null=True)
    video = models.FileField(upload_to='gallery/videos/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return f"{self.look.title or self.look.category} - {self.media_type}"