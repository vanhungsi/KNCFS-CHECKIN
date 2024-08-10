from django.db import models
from django.utils import timezone
from factory.models import Factory


class Checkin(models.Model):
    driver_name = models.CharField("Họ và tên", max_length=32)
    truck_number = models.CharField("Số xe/số container", max_length=32)
    phone_number = models.CharField("Số điện thoại", max_length=32)
    checkin_time = models.DateTimeField("Giờ check-in", default=timezone.now)
    factory = models.ForeignKey(Factory, blank=True, null=True, on_delete=models.CASCADE)
    shipper = models.CharField("Chủ hàng", max_length=100, blank=True, null=True)
    remark = models.TextField("Ghi chú", max_length=1024, blank=True, null=True)

    def __str__(self):
        factory_code = self.factory.factory_code
        return f"{self.truck_number} - {factory_code} - {self.checkin_time1.strftime('%Y-%m-%d %H:%M:%S')}"

    def clean(self):
        from django.core.exceptions import ValidationError
        if self.factory is None:
            raise ValidationError({'factory': 'This field cannot be null.'})

