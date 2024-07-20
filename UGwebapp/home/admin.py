from django.contrib import admin
from .models import Item_Category, Item, Claim


# This part registers the models to the Django adminSite 
@admin.register(Item_Category)
class Item_CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'status', 'created', 'updated']
    list_filter = ['status', 'created', 'updated']
    list_editable = ['status']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ['item', 'claimant', 'date_claimed', 'status']
    list_filter = ['status', 'date_claimed']

# Register your models here.
