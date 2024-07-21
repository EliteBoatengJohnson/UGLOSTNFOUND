from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Item_Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    class Meta:
        ordering =['name']
        indexes = [models.Index(fields=['name']),]
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
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='reporter')
    #price = models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
        ordering =['-created']
        indexes = [models.Index(fields=['id','slug']),
                   models.Index(fields=['name']),
                   models.Index(fields=['-created']),
                   ]
    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"
    


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
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Claim for {self.item.title} by {self.claimant.username}"
    


class Report(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='reports')
    reporter = models.ForeignKey(User, on_delete=models.CASCADE,related_name='reports'  )
    date_reported = models.DateTimeField(auto_now_add=True)
    additional_info = models.TextField(blank=True)