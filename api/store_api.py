from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from store.services import validate_store_login
import json


@csrf_exempt
def StoreLogin(request):
    if request.method == "POST":
        r = request.body
        json_data = json.loads(str(r, encoding='utf-8'))
        code = json_data['code']
        password = json_data['password']

        valid = validate_store_login(code, password)

        if valid:
            status = 200
        else:
            status = 404
    else:
        status = 400

    return JsonResponse({
        "status": status
    })



