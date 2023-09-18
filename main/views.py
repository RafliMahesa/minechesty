from django.http import HttpResponseRedirect
from main.forms import ItemForm
from django.urls import reverse
from django.shortcuts import render
from main.models import Item
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_main(request):
    item = Item.objects.all()
    total_item = 0
    for i in item:
        total_item += 1

    context = {
        'app_name' : 'MineChesty',
        'name' : 'Muhammad Rafli Mahesa',
        'class': 'PBP E',
        'item' : item,
        'total' : total_item
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        print("test")
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


    