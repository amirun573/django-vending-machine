# vending_machine_app/views.py
from django.shortcuts import render, redirect
from .models import Item

def vending_machine(request):
    items = Item.objects.all()

    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        try:
            item = Item.objects.get(pk=item_id)
            if request.user.profile.coins >= item.price:
                request.user.profile.coins -= item.price
                request.user.profile.save()
                return render(request, 'vending_machine/purchase_success.html', {'item': item})
            else:
                return render(request, 'vending_machine/purchase_failure.html', {'item': item})
        except Item.DoesNotExist:
            pass

    return render(request, 'vending_machine/vending_machine.html', {'items': items})
