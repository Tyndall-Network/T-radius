from django.db import models

# Create your models here.


class Nas(models.Model):
    """A network Access Server.

    ie: ISP Router, eduroam Access Point etc.
    """

    # id = models.IntegerField(primary_key=True) Django creates
    # automatic Primary Keys, only add to change behaviour
    name = models.CharField(max_length=32)
    manufacturer = models.CharField(max_length=16, default="MikroTik")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField(protocol="both")
