from shortener.models import UrlMapping
from django import forms


class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlMapping
        fields = ["original_url"]
