# vending_machine_app/views.py
from django.shortcuts import render, redirect
from .models import Item
from django.http import HttpResponse,JsonResponse
import json

items = [{
    "id": 1,
    "name": 'Cholocate',
    "price": 20.00,
    "image_path": "public/images/chocolate-gda6c41870_1280.jpg",
},
{
    "id": 2,
    "name": 'Coke',
    "price": 5.00,
    "image_path": "public/images/drink-g078419792_1280.jpg",
},
{
    "id": 3,
    "name": 'Chip',
    "price": 4.00,
    "image_path": "public/images/french-fries-gcf12f4685_1280.jpg",
},
{
    "id": 4,
    "name": 'Snicker',
    "price": 6.00,
    "image_path": "public/images/snickers-ga4ff864cb_1280.jpg",
},
{
    "id": 5,
    "name": 'Pepsi',
    "price": 2.00,
    "image_path": "public/images/pepsi-gc651f7aa7_1280.jpg",
}

]


def vending_machine(request):
  

    return render(request, 'vending_machine/vending_machine.html', {'items': items})

def submit_item(request):

    data = request.body.decode('utf-8')

    # Parse the JSON data to a Python dictionary
    data = json.loads(data)
    items_purchase = data.get('itemsPurchase', [])
    input_amount = data.get('inputAmount', 0)

    if(len(items_purchase) <0):
        return JsonResponse({"error": "Invalid JSON data."}, status=400)
    
    if(input_amount < 0):
        return JsonResponse({"error": "Invalid JSON data."}, status=400)
    
    total_price = 0

    for item in items_purchase:
        item_id = item.get('id', None)
        quantity = item.get('quantity', None)

        item_details = find_items(item_id)

        if(item_details == None):
            return JsonResponse({"error": "Invalid JSON data."}, status=400)

        total_price = total_price + (item_details["price"] * quantity)

    # Calculate the balance
    balance = input_amount - total_price

    # Convert the balance to a string
    balance_str = str(balance)
        
    message = f"Thank You. Please Enjoy Your Meals. Here is the Balance: (RM) {balance_str}"
    if(input_amount - total_price >=0):
        return JsonResponse({"message": message}, status=200)


def find_items(id):
    for item in items:
        if id == item["id"]:
            return item
    
    return None
