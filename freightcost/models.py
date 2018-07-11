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


class Skin(models.Model):
    '''用户上传的皮肤'''
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # skin_title = models.CharField(max_length=255,verbose_name="皮肤名")
    skin_path = models.TextField(verbose_name="皮肤路径")
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name ="皮肤"
        verbose_name_plural = verbose_name

    def __str__(self):
        '''返回模型的字符串'''
        return self.skin_path