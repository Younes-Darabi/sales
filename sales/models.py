from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=30, help_text="Max 30 letters")
    last_name = models.CharField(max_length=30)
    newsletter_abo = models.BooleanField(default=True)
    email_address = models.EmailField(max_length=30, blank=True, default="")
    account = models.FloatField(blank=True, null=True)
    slug = models.SlugField(blank=True, default="")

    class Meta:
        verbose_name = "مشتری"
        verbose_name_plural = "مشتری ها"
        ordering = ["-account"]

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.account} "

    def save(self):
        self.account = 651681
        return super().save()