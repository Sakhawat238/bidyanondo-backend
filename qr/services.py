from .models import QrLog, QrRewardLog
from store.models import Store


def check_qr_exists(code, timestamp):
    if QrLog.objects.filter(code=code, timestamp=timestamp).exists():
        return True
    return False


def claim_rewards(code, timestamp, quantity, store, items):
    if check_qr_exists(code, timestamp):
        return False
    try:
        storeid = Store.objects.filter(code=store).first().id
        QL = QrLog(code=code, timestamp=timestamp, quantity=quantity, store_id=storeid)
        QL.save()

        rewards_list = []
        for item in items:
            rewards_list.append(QrRewardLog(qr_id=QL.id, item_id=item))
        QrRewardLog.objects.bulk_create(rewards_list, batch_size=50)

        return True
    except:
        return False