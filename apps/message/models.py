# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class UserMessage(models.Model):
    # 设置最大长度， verbose_name 在后台显示字段会用到
    name = models.CharField(max_length=20, verbose_name='user')
    email = models.EmailField(verbose_name='email')
    address = models.CharField(max_length=100, verbose_name='address')
    message = models.CharField(max_length=500, verbose_name='msg_address')

    class Meta:
        verbose_name = 'user_msg'
