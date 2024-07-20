from django.db import models
from django.contrib.auth.models import User

class Item_Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering =['name']
        index = [models.Index(fields=['name']),]
        verbose_name = 'Item_Category'
        verbose_name_plural = 'categories'
def __str__(self):
    return self.name



#product == item
class Item(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found'),
        ('claimed', 'Claimed'),]
    category =models.ForeignKey(Item_Category,related_name='Item', on_delete=models.CASCADE)
    name =models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')
    image = models.ImageField(upload_to='items/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #price = models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        odering =['name']
        indexes = [models.Index(fields=['id','slug']),
                   models.Index(fields=['name']),
                   models.Index(fields=['-created']),
                   ]
    def __str__(self):
        return self.name
    


class Claim(models.Model):
    CLAIM_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='claims')
    claimant = models.ForeignKey(User, on_delete=models.CASCADE)
    date_claimed = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    status = models.CharField(max_length=10, choices=CLAIM_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Claim for {self.item.title} by {self.claimant.username}"