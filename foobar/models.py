from django.db import models

# Create your models here.

class Tab(models.Model):
    owner = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    bar_name = models.CharField(max_length=30)
    active = models.BooleanField()


class Items(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    items = models.ForeignKey(Tab,on_delete=models.CASCADE, related_name='items')

    def __unicode__(self):
        return '%s: %d' % (self.name, self.price)
