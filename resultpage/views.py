from django.shortcuts import render
from .models import Menu

# Create your views here.
def index(request):

    kafka_data = Menu.objects.all()

    context = {'kafka_db_data': kafka_data}

    return render(request, 'result.html', context)