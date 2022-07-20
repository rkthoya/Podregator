from django.views.generic import ListView

from .models import Content


class HomePageView(ListView):
    template_name = "homepage.html"
    model = Content

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Content.objects.filter().order_by("-pub_date")[:20]
        return context
