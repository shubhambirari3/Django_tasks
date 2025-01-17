from django.db import models

class WebsiteInfo(models.Model):
    site_name = models.CharField(max_length=255)
    url = models.URLField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.site_name
