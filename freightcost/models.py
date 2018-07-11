from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


# Create your models here.
# class Topic(models.Model):
#     '''用户学习的主题'''
#     text = models.CharField(max_length=200)
#     date_add = models.DateTimeField(auto_now_add=True)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         '''返回模型的字符串'''
#         return self.text

#

class Entry(models.Model):
    '''司机提交报销的详细信息'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bxno = models.BigAutoField(primary_key=True, verbose_name="报销编号")
    title = models.CharField(max_length=20, verbose_name="报销事项")
    carNo = models.CharField(max_length=20, verbose_name="车牌号")
    text = models.TextField(verbose_name="备注")
    amout = models.DecimalField(max_digits=9, decimal_places=2, verbose_name="金额")
    img = models.ImageField(upload_to="media/img", verbose_name="发票图片")
    wipeout = models.BooleanField(default=False, blank=True, verbose_name="核销状态")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '报销详情表'
        verbose_name_plural = verbose_name

    def __str__(self):
        '''返回模型的字符串'''
        return self.title + ": " + self.text[:40] + "..."
