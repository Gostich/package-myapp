from django.http import HttpResponse

from .models import Place
from .utils import format_hello


def hello_world(request):
    hello_list = [format_hello(place.name) for place in Place.objects.all()]
    if not hello_list:
        return HttpResponse("No place :-(")
    return HttpResponse(" - ".join(hello_list))
