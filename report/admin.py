from django.contrib import admin
from django.shortcuts import render
from django.db.models import Prefetch
from .models import RewardHistory
from store.models import Store
from qr.models import QrLog, QrRewardLog


@admin.register(RewardHistory)
class RewardHistoryAdmin(admin.ModelAdmin):
    change_list_template = 'reward_history_input.html'
    def changelist_view(self, request, extra_context=None):
        if request.method == "POST":
            r = request.POST
            store_id = r.get('store-select')
            start = r.get('from-date')
            end = r.get('to-date')

            qrlogs = QrLog.objects.prefetch_related(Prefetch('qrrewardlog_set',
                queryset=QrRewardLog.objects.select_related('item').all(),
                to_attr="reward_items")).select_related('store').all()

            if store_id is not None and store_id != "":
                qrlogs = qrlogs.filter(store_id=store_id)
            if start is not None and start != "":
                qrlogs = qrlogs.filter(when_used__date__gte=start)
            if end is not None and end != "":
                qrlogs = qrlogs.filter(when_used__date__lte=end)                
            
            rewards = []
            for ql in qrlogs:
                rewards.append({
                    "store": ql.store.name,
                    "code": ql.code,
                    "timestamp": ql.timestamp,
                    "quantity": ql.quantity,
                    "applied": ql.when_used,
                    "items": ql.reward_items
                })

            context = {
                'rewards': rewards
            }
            return render(request, "reward_history.html", context)
        else:
            stores = Store.objects.values('id', 'name')
            context = {
                'stores': stores
            }
            return render(request, "reward_history_input.html", context)
