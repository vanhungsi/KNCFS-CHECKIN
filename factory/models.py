from django.db import models

class Factory(models.Model):
    factory_code = models.CharField(max_length=10, null=True, blank=True)
    factory_name = models.CharField(max_length=256)


    def __str__(self):
        return f"{self.factory_code} | {self.factory_name}"


