from django.contrib import admin
from .models import Reward, Item, RewardItem


admin.site.register(Reward)
admin.site.register(Item)
admin.site.register(RewardItem)