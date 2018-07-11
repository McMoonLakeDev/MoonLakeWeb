from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # # 特定主题的详细页面
    # url(r'^entries/$', views.entries, name='entries'),
    url(r'^MySkin/$', views.my_skin, name='MySkin'),
    #
    # #用于添加新主题的网页
    # url(r'^new_topic/$',views.new_topic,name='new_topic'),

    # 用于添加新条目的页面
    # url(r'^new_entry/$', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    # url(r'^ChangSkin/(?P<entry_id>\d+)/$', views.edit_my_skin,
    #     name='ChangSkin'),
    #
    # #更改用户语言
    # url(r'^change_language/(?P<language>[A-Za-z0-9\-]+)/$',views.change_language,
    #     name='change_language'),
]

app_name = 'freightcost'
