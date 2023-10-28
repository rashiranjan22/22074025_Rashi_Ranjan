from django.db import models

# Create your models here.
# shortener/models.py
from django.db import models
import shortuuid

class ShortURL(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = shortuuid.uuid()[:8]
        super().save(*args, **kwargs)