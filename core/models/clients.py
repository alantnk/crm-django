from django.db import models
from django.conf import settings
from django_resized import ResizedImageField
from .base import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Client(BaseModel):
    fantasy_name = models.CharField(max_length=100)
    office_name = models.CharField(max_length=100)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    idoc = models.CharField(max_length=20, unique=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, null=True)
    location = models.CharField(max_length=100, null=True)
    state_code = models.CharField(max_length=3, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    district = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)

    cover = ResizedImageField(
        size=[640, 480], upload_to="clients/covers/%Y/%m/", blank=True, null=True
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_clients",
        null=True,
    )

    user_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="edited_clients",
        null=True,
    )

    def __str__(self):
        return self.fantasy_name


class Position(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Contact(BaseModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, null=True)
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True)
    location = models.CharField(max_length=100, null=True)
    district = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="created_contacts",
        null=True,
    )
    user_editor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name="edited_contacts",
        null=True,
    )

    def __str__(self):
        return self.full_name
