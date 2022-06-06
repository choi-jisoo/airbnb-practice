from django.db import models
from core import models as core_models


class Review(core_models.TimeStampedModel):

    """Review Model Definition"""

    review = models.TextField()
    accuracy = models.IntegerField()
    cleanliness = models.IntegerField()
    check_in = models.IntegerField()
    communication = models.IntegerField()
    location = models.IntegerField()
    value = models.IntegerField()
    user = models.ForeignKey(
        "users.User", related_name="reviews", on_delete=models.CASCADE
    )
    room = models.ForeignKey(
        "rooms.Room", related_name="reviews", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.review} - {self.room}"

    def rating_average(self):
        avg = (
            self.accuracy
            + self.cleanliness
            + self.check_in
            + self.communication
            + self.location
            + self.value
        ) / 6
        return round(avg, 2)

    rating_average.short_description = "Avg."
