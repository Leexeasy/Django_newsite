from django.shortcuts import render
from mysite.models import Product
from django.http import HttpResponse,Http404
from django.template.loader import get_template
import random
# Create your views here.
def about(request):
    template = get_template('about.html')

    html = template.render()
    return HttpResponse(html)
def listing(request):

    template = get_template('list.html')
    products = Product.objects.all()
    html = template.render({'products':products})
    return HttpResponse(html)
def disp_detail(request,sku):

    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定的产品编号')



    template = get_template('disp.html')
    html = template.render({'product':p})
    return HttpResponse(html)
def index(request):
    template = get_template('index.html')
    quotes = ['今日事，今日毕',
              '没有付出，没有收获',
              '知识就是力量',
              '一个人的个性就是他的命运',
              ]
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)