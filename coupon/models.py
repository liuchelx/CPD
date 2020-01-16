from django.db import models
import hashlib

STATUS_LIST = [
    ("new", 1),
    ("used", 0)
]


class Coupon(models.Model):
    name = models.CharField(max_length=300)
    # coupon_code = models.CharField(max_length=8) #todo:
    # todo: we do not generate coupon code for now, use id as coupon code for now
    # todo: QR code in the future
    discount = models.IntegerField()
    discount_test = models.CharField(max_length=100,default=discount)
    value = models.FloatField(default=0)
    modified_by = models.CharField(max_length=100)
    send_to = models.CharField(max_length=100,default='null')
    modified_at = models.DateTimeField('modified_Date')
    created_at = models.DateTimeField(auto_now_add=True)
    state = models.CharField(choices=STATUS_LIST, default='new', max_length=50)

    def CouponCode(self):
        code = str(self.name)+str(self.discount)+str(self.created_at)
        couponCode = abs(hash(code)) % (10 ** 8)
        return couponCode


    def __str__(self):
        return self.name