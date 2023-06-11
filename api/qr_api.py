from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from qr.services import check_qr_exists
from reward.services import get_reward_items
import json


@csrf_exempt
def QrSearch(request):
    r = request.body
    json_data = json.loads(str(r, encoding='utf-8'))
    code = json_data['code']
    timestamp = json_data['timestamp']
    quantity = json_data['quantity']

    if check_qr_exists(code, timestamp):
        return JsonResponse({
            "status": 400,
            "message": "QR code has already been used."
        })

    return get_reward_items(quantity)