import django.db
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from shortener.forms import UrlForm
from shortener.shortener import Shortener
from shortener.models import UrlMapping
from django.contrib import messages


def redirect_to_original_url(request, token):
    url_map = UrlMapping.objects.filter(short_url=token)[0]
    return redirect(url_map.original_url)


class Index(CreateView):
    template_name = "shortener/base.html"
    form_class = UrlForm

    def form_valid(self, form):
        new_url = form.save(commit=False)

        while True:
            token = Shortener().generate_token()
            new_url.short_url = token

            try:
                new_url.save()
            except django.db.IntegrityError:
                continue
            else:
                token = new_url.short_url
                messages.add_message(self.request, messages.SUCCESS, "Success")
                hostname = self.request.build_absolute_uri("/")

                return render(
                    self.request,
                    "shortener/base.html",
                    {"token": token, "form": form, "hostname": hostname},
                )
