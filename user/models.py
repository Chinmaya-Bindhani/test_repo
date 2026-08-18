from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=155)
    description = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)# auto_now_add = true (updates only while first time creation of the object )
    updated_at=models.DateTimeField(auto_now=True) # auto_now = true (updates every time the object is created )

    def __str__(self):
        return self.name

