from django.db import models

class Publication(models.Model):
    slug = models.SlugField()
    pub_date = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.slug
