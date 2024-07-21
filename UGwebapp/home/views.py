from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Item_Category, Claim
#from .forms import ItemForm, ClaimForm

def home(request):
    categories = Item_Category.objects.all()
    recent_items = Item.objects.filter(status='found').order_by('-date_found')[:10]
    return render(request, 'home/home.html', {'categories': categories, 'recent_items': recent_items})

def item_list(request, category_slug=None):
    category = None
    items = Item.objects.filter(status='found')
    if category_slug:
        category = get_object_or_404(Item_Category, slug=category_slug)
        items = items.filter(category=category)
    return render(request, 'home/item_list.html', {'category': category, 'items': items})

@login_required
def report_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.reporter = request.user
            item.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = ItemForm()
    return render(request, 'home/report_item.html', {'form': form})

def item_detail(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    return render(request, 'home/item_detail.html', {'item': item})

@login_required
def claim_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ClaimForm(request.POST)
        if form.is_valid():
            claim = form.save(commit=False)
            claim.item = item
            claim.claimant = request.user
            claim.save()
            return redirect('item_detail', item_id=item.id)
    else:
        form = ClaimForm()
    return render(request, 'home/claim_item.html', {'form': form, 'item': item})