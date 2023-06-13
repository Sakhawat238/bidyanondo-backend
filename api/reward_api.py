from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from qr.services import claim_rewards
import json


@csrf_exempt
def RewardClaim(request):
    r = request.body
    json_data = json.loads(str(r, encoding='utf-8'))
    code = json_data['code']
    timestamp = json_data['timestamp']
    quantity = json_data['quantity']
    store = json_data['store']
    rewards = json_data['rewards']

    success = claim_rewards(code, timestamp, quantity, store, rewards)

    return JsonResponse({
        "success": success
    })
