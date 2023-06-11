from django.db import models


class Reward(models.Model):
    quantity = models.PositiveIntegerField(null=False)

    def __str__(self):
        return str(self.quantity)



class Item(models.Model):
    description = models.CharField(max_length=250, null=False)
    
    def __str__(self):
        return self.description


class RewardItem(models.Model):
    reward = models.ForeignKey(Reward, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return str(self.reward.quantity) + " : " + self.item.description

