from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass

class Categgory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)


    def __str__(self):
        return self.name
    

class Item(models.Model):
    item_name = models.CharField(max_length=20)
    description =models.TextField()
    category = models.ForeignKey(Categgory, on_delete=models.CASCADE, related_name='items')
    location = models.CharField(max_length=200)
    lost_date = models.DateTimeField()
    found_date = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True,related_name='found_items')
    found_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,blank=True,related_name='claimed_items')
    status = models.CharField(max_length=20, choices=[('lost','Lost'),('found','Found'),('claimed','Claimed'),('returned',"Returned")])
    image = models.ImageField(upload_to='/item_images',blank=True,null=True)

    def __str__(self):
        return self.item_name
    

class Owner(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='owner')
    message = models.TextField()
    recipient = models.ForeignKey(User,on_delete=models.CASCADE,related_name='owners')
    is_read = models.BooleanField(default=False)

class Finder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='finder')
    items = models.ManyToManyField(Item,related_name='finders')


class Notification(models.Model):
    item = models.ForeignKey(Item,on_delete=models.CASCADE,related_name='notifications')
    message =models.TextField()
    recipient = models.ForeignKey(User,on_delete=models.CASCADE,related_name='notifications')
    is_read = models.BooleanField(default=False)


class Claim(models.Model):
    item= models.ForeignKey(Item,on_delete=models.CASCADE,related_name='claims')
    owner = models.ForeignKey(Owner,on_delete=models.CASCADE,related_name='claims')
    Finder= models.ForeignKey(Finder,on_delete=models.CASCADE,related_name='claims')
    status = models.CharField(max_length=20,choices=[('pending','Pending'),('accepted','Accepted'),('rejected','Rejected')])
    date_claimed = models.DateField(auto_now_add=True)


