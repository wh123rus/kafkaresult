from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Menu

def index(request):
    item_list = ['Nike', 'Adidas', 'Newbalance', 'Salomon', 'Jordan', 'Converse']
    
    # 현재 필터링 상태 확인
    item_filter = request.POST.get('item_filter') or request.GET.get('item_filter', '')

    if item_filter:
        kafka_data = Menu.objects.filter(item=item_filter)
    else:
        kafka_data = Menu.objects.all()

    # 페이징 추가
    paginator = Paginator(kafka_data, 20)  # 한 페이지에 10개의 항목을 보여줍니다.
    page = request.GET.get('page')

    try:
        kafka_data = paginator.page(page)
    except PageNotAnInteger:
        # 페이지 번호가 정수가 아닌 경우, 첫 번째 페이지를 보여줍니다.
        kafka_data = paginator.page(1)
    except EmptyPage:
        # 페이지가 비어 있는 경우, 마지막 페이지를 보여줍니다.
        kafka_data = paginator.page(paginator.num_pages)

    context = {'kafka_db_data': kafka_data, 'item_list': item_list, 'current_item_filter': item_filter}

    return render(request, 'result.html', context)