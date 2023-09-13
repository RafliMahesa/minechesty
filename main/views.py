from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name' : 'MineChesty',
        'name' : 'Muhammad Rafli Mahesa',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)