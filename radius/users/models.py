from django.db import models
import uuid
# Create your models here.


class User(models.Model):
    """User class."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=16)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Level = models.IntegerChoices("Level", "ADMIN RESELLER ISP USER")
    user_level = models.IntegerField(choices=Level.choices, default=Level.USER)
