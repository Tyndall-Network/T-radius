from django.db import models

# Create your models here.


class Plan(models.Model):
    """Data Plan Class.

    download: Download calculated in octets(stored as integers) by
                radius server
            Can be used for both aggregative & unlimited data plans therefore
                dependent on implementation
    upload: Same as download.
    """

    HOURLY = "hr"
    DAILY = "dl"
    WEEKLY = "wk"
    MONTHLY = "mn"
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    download = models.IntegerField(default=0)
    upload = models.IntegerField(default=0)
    period = models.CharField(max_length=2,
                              choices=[(HOURLY, "hourly"), (DAILY, "daily"),
                                       (WEEKLY, "weekly"),
                                       (MONTHLY, "monthly")],
                              default=MONTHLY
                              )
    cost = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
