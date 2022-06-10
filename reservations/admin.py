from django.contrib import admin
from . import models


class CustomListFilter(admin.SimpleListFilter):
    title = "In Progress"
    parameter_name: str = "in_progress"

    def lookups(self, request, model_admin):
        return (
            ("True", "True"),
            ("False", "False"),
        )

    def queryset(self, request, queryset):
        now = models.get_now_date()
        if self.value() == "True":
            return queryset.filter(check_in__lte=now, check_out__gte=now)
        elif self.value() == "False":
            return queryset.exclude(check_in__lte=now, check_out__gte=now)


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):

    """Reservation Admin Definition"""

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "in_progress",
        "is_finished",
    )

    list_filter = (
        "status",
        CustomListFilter,
    )
