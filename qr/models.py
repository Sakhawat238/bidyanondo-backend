from django.db import models
from store.models import Store
from reward.models import Item


class QrLog(models.Model):
    code = models.CharField(max_length=100, null=False)
    timestamp = models.CharField(max_length=30, null=False)
    quantity = models.PositiveIntegerField(null=False)
    when_used = models.DateTimeField(auto_now_add=True)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.code + "_" + self.timestamp


class QrRewardLog(models.Model):
    qr = models.ForeignKey(QrLog, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.qr.code + " : " + self.item.description