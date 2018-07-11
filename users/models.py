from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    rolechoice = (
        (1,"司机"),
        (2,"会计"),
        (3,"管理员"),
    )
    realname = models.CharField(max_length=50, null=False, default="未注册真实姓名 ", blank=True, verbose_name="真实姓名")
    role = models.IntegerField(default=1, null=False, verbose_name="用户角色", choices=rolechoice)

    class Meta(AbstractUser.Meta):
        pass
