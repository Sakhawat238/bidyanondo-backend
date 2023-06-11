from django.contrib import admin
from .models import QrLog, QrRewardLog

admin.site.register(QrLog)
admin.site.register(QrRewardLog)
