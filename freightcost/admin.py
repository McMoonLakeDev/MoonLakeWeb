from django.contrib import admin
from freightcost.models import Skin
from users.models import User
from django.conf import settings

# Register your models here.

admin.site.register(User)
admin.site.register(Skin)
