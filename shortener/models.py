from django.db import models


class UrlMapping(models.Model):
    original_url = models.URLField(verbose_name="Original URL")
    short_url = models.CharField(max_length=6, unique=True, verbose_name="Short URL")

    class Meta:
        db_table = "url_mapping"
        verbose_name = "Url Mapping"
