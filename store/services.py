from .models import Store


def validate_store_login(code, password):
    if Store.objects.filter(code=code, password=password).exists():
        return True
    return False