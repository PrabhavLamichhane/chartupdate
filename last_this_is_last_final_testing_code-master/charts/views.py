from django.shortcuts import render
from django.db.models import Count, Q
from registration.models import Account
from datetime import datetime
from django.utils import timezone
from datetime import date
from django.db.models.functions import ExtractMonth
# Create your views here.


# def bar_graph(request):
#     return render(request, 'chart.html')

today = date.today()


def bar_graph(request):

    dataset = Account.objects.values('email') .annotate(user_count=Count(
        'email', filter=Q(is_active=True))).order_by('date_joined')

    print(dataset)
    return render(request, 'chart.html', {'dataset': dataset})
