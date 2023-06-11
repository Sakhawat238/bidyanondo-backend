from .models import QrLog


def check_qr_exists(code, timestamp):
    if QrLog.objects.filter(code=code, timestamp=timestamp).exists():
        return True
    return False