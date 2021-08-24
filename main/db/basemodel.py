from django.db import models


class BaseModel(models.Model):
    """Base model to be used to inject common fields.
    """
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    modified_at = models.DateTimeField(
        auto_now=True
    )

    is_active = models.BooleanField(
        default=True
    )

    class Meta:
        abstract = True