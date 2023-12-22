from django.urls import path
from shortener import views


urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path(
        "<str:token>", views.redirect_to_original_url, name="redirect_to_original_url"
    ),
]
