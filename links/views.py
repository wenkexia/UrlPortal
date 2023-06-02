from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, Http404
from django.http import HttpResponseRedirect
from . import models


# 视图函数中使用 Django ORM 的查询语句来获取与该短链接对应的所有原始链接，然后在 Python 中随机选择一个返回
def redirect_to_original(request, short_code):
    # 根据 short_code 查询是否存在对应的 Link 对象
    link = get_object_or_404(models.Link, short_url=short_code, is_enabled=1)
    # 获取与该 Link 对象对应的所有 Url 对象
    urls = link.url_set.filter(is_enabled=1)
    if not urls:
        raise Http404()
    # 随机返回一个 Url 的 original_url 属性值
    redirect_to = urls.order_by('?').first().original_url
    # 重定向到原始链接
    return HttpResponseRedirect(redirect_to)
