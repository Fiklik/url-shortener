from django.db import models


class UrlMapping(models.Model):
    original_url = models.URLField()
