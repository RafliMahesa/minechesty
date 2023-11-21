import datetime
import json 

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages  
from django.http import HttpResponseNotFound, HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers

from main.forms import ItemForm
from main.models import Item

# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    item = Item.objects.filter(user=request.user)
    total_item = 0
    for i in item:
        total_item += 1

    if ('last_login' not in request.COOKIES):
        return login_user(request)

    context = {
        'app_name' : 'MineChesty',
        'name' : request.user.username,
        'class': 'PBP E',
        'item' : item,
        'total' : total_item,
        'last_login': request.COOKIES['last_login'][:-10]
    }

    return render(request, "main.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def create_product(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
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

def tambah_amount(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.amount += 1
        item.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def kurang_amount(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        if item.amount > 0:
            item.amount -= 1
            item.save()
        if item.amount == 0:
            item.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def hapus_item(request, id):
    if request.method == "POST":
        item = Item.objects.get(pk=id)
        item.delete()
    return HttpResponseRedirect(reverse('main:show_main')) 

def edit_item(request, id):
    # Get product berdasarkan ID
    item = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_item_json(request):
    item = Item.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize('json', item))

@csrf_exempt
def add_item_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        amount = request.POST.get("amount")
        description = request.POST.get("description")
        rarity = request.POST.get("rarity")
        user = request.user

        new_item = Item(name=name, amount=amount, description=description, rarity = rarity, user=user)
        new_item.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_item_ajax(request, id):
    if request.method == 'DELETE':
        Item.objects.get(pk=id).delete()
        return HttpResponse(b"DELETED", status = 201)
    return HttpResponseNotFound()
    
@csrf_exempt
def create_item_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            description = data["description"],
            amount = int(data["amount"]),
            rarity = data["rarity"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)