from django.shortcuts import render
from .models import Menu
from django.core.paginator import Paginator  

# Create your views here.
def index(request):
    page = request.GET.get('page', '1')  # 페이지

    kafka_data = Menu.objects.all()

    paginator = Paginator(kafka_data, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    
    context = {'kafka_db_data': page_obj}

    return render(request, 'index.html', context)