from django.views.generic import ListView, DetailView
from . import models


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
    page_kwarg = "page"


class RoomDetail(DetailView):

    """RoomDetail Definition"""

    model = models.Room
