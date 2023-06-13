from django.http import JsonResponse
from .models import Reward, RewardItem


def get_reward_items(quantity):
    reward = Reward.objects.filter(quantity__lte=quantity).order_by('-quantity').first()
    rewarditems = list(RewardItem.objects.select_related('item').filter(reward=reward).values('item_id','item__description'))
    if len(rewarditems) > 0:
        return JsonResponse({
            "status": 200,
            "quantity": reward.quantity,
            "data": rewarditems
        })
    
    return JsonResponse({
        "status": 400,
        "message": "Quantity is not sufficient enough for reward."
    })