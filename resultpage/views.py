from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request):
    item_list = ['Nike', 'Adidas', 'Newbalance', 'Salomon', 'Jordan', 'Converse']
    
    if request.method == 'POST':
        item_filter = request.POST.get('item_filter')
        if item_filter:
            kafka_data = Menu.objects.filter(item=item_filter)
        else:
            kafka_data = Menu.objects.all()
    else:
        kafka_data = Menu.objects.all()

    context = {'kafka_db_data': kafka_data, 'item_list': item_list}

    return render(request, 'result.html', context)