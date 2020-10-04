from django.db import models
from custom_content.model_unique_key import RandomPrimaryIdModel


class TimeStampMixin(models.Model):
    """Mixin to add dates for creation and last date modified."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PlainText(RandomPrimaryIdModel, TimeStampMixin):
    """Example for Django model, that gets registered in wagtail Admin."""

    plain_text = models.CharField(
        null=False,
        blank=False,
        max_length=2000,
        help_text="This is just meant for plain text as an example.",
    )

    class Meta:
        verbose_name = "Plain Text"
        verbose_name_plural = "Plain Texts"

    def __str__(self):
        return self.plain_text
