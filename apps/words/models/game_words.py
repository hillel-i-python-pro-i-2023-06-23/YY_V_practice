from django.db import models


class GameWords(models.Model):
    name_of_gamer = models.CharField(max_length=100)
    word = models.CharField(max_length=100)

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        null=False,
    )

    def __str__(self) -> str:
        return f"{self.name_of_gamer}"

    __repr__ = __str__

    class Meta:
        ordering = ["-created_at", "name_of_gamer"]
