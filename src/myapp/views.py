from django.http import HttpResponse

from .models import Place


def hello_world(request):
    hello_list = [f"Hello {place}" for place in Place.objects.all()]
    if not hello_list:
        return HttpResponse("No place :-(")
    return HttpResponse(" - ".join(hello_list))
