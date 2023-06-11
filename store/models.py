from django.db import models



class Store(models.Model):
    code = models.CharField(max_length=15, null=False)
    password = models.CharField(max_length=15, null=False)
    name = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=250, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    is_archived = models.BooleanField(default=False)


    def __str__(self):
        return self.code
