from django.db import models
from django.contrib.auth.models import User
import hashlib
import base64
import shortuuid  # 需要先安装 shortuuid 库
import re



class Link(models.Model):

    id = models.AutoField(primary_key=True)
    short_url = models.CharField(max_length=10, unique=True,verbose_name='短链接')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    STATUS_CHOICES = (
        (0, '未启用'),
        (1, '启用'),
    )
    is_enabled = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='启用状态')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.short_url


    class Meta:
        verbose_name = '短链接'
        verbose_name_plural = '短链接'


class Url(models.Model):
    id = models.AutoField(primary_key=True)
    original_url = models.URLField(max_length=200, verbose_name='原始链接')
    description = models.CharField(max_length=200, blank=True, verbose_name='描述')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    STATUS_CHOICES = (
        (0, '未启用'),
        (1, '启用'),
    )
    is_enabled = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='启用状态')
    link = models.ForeignKey(Link, on_delete=models.CASCADE, verbose_name='短链接')
    class Meta:
        # 来确保数据库中的 url, link 唯一性。
        unique_together = ('original_url', 'link')
        verbose_name = '原始链接'
        verbose_name_plural = '原始链接'

    def __str__(self):
        return self.original_url