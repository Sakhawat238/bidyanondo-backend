from django.db import models

class RewardHistory(models.Model):
    id = models.BigAutoField(db_column='id', primary_key=True)

    def __str__(self):
        return "<Label: id: %d>" % self.id