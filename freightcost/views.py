from django.shortcuts import render
from .models import Skin
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# from .form import SkinForm
from django.conf import settings
from PIL import Image
import hashlib


# Create your views here.
def index(request):
    '''月色之湖首页'''
    return render(request, 'freightcost/index.html')


@login_required
def my_skin(request):
    '''显示自己的皮肤'''

    # 获取自己的皮肤数据
    my_skin = Skin.objects.filter(owner=request.user).order_by("-date_added")
    # 如果没有皮肤，就用默认皮肤，如果有皮肤就使用自己的皮肤
    skin_url = ""
    print(my_skin)
    if len(my_skin) == 0:
        skin_url = settings.SKIN_DIR + "default.png"
    else:
        skin_url = my_skin[0].skin_path
        print(my_skin[0].skin_path)


    # POST提交数据就对其进行处理
    if request.method == 'POST':
        # 获得用户提交的图片数据
        getpng = request.FILES.get('fileinput')

        #获取上传的图片实例，同时会自动检测是否是有效图片，防止被利用解析漏洞
        img = Image.open(getpng)
        #判断是否是png图片，判断像素是否是64*64和64*32.
        if img.format == "PNG":
            if img.size == (64, 64) or img.size == (64, 32):
                img_name = hashlib.sha256(img.tobytes()).hexdigest().lower()
                if settings.SKIN_DIR[-1] == "/" or settings.SKIN_DIR[-1] == "\\":
                    img_path = settings.SKIN_DIR + img_name + ".PNG"
                else:
                    img_path = settings.SKIN_DIR + "/" + img_name + ".PNG"
                print(img_path)

                #保存图片，同时保存图片路径
                try:
                    img.save(settings.MEDIA_ROOT + img_path)  # 路径(绝对/相对)
                    Skin.objects.create(skin_path=img_path, owner=request.user)
                except:
                    pass

        # print(img.format)
        return HttpResponseRedirect(reverse('freightcost:MySkin'))

    context = {'my_skin': my_skin, "skin_url": skin_url, }
    return render(request, 'freightcost/viewSkin.html', context)

# @login_required
# def entry(request, entry_id):
#     '''显示当前皮肤'''
#     entry = Entry.objects.get(bxno=entry_id)
#     # 确认请求的皮肤属于当前用户
#     if entry.owner != request.user:
#         raise Http404
#     context = {'entry': entry}
#     return render(request, 'freightcost/entry.html', context)
#


# @login_required
# def new_entry(request):
#     if request.method != 'POST':
#         # 未提交数据，创建一个空表单
#         form = EntryLowForm()
#     else:
#         form = EntryLowForm(request.POST or None, request.FILES or None)
#
#         if form.is_valid():
#             new_entry = form.save(commit=False)
#             new_entry.owner = request.user
#
#             new_entry.save()
#             return HttpResponseRedirect(reverse('freightcost:entries'))
#     context = {'form': form}
#     return render(request, 'freightcost/new_entry.html', context)

#
# @login_required
# def edit_my_skin(request, entry_id):
#     '''
#     编辑既有条目
#     :param request:
#     :param entry_id:
#     :return:
#     '''
#     entry = Entry.objects.get(bxno=entry_id)
#
#     if entry.owner != request.user:
#         raise Http404
#
#     if request.method != 'POST':
#         # 初次请求建立表单
#         form = EntryLowForm(instance=entry)
#     else:
#         # POST提交数据就对其进行处理
#         form = EntryLowForm(instance=entry, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('freightcost:entry',
#                                                 args=[entry.bxno]))
#
#     context = {'entry': entry, 'form': form}
#     return render(request, 'freightcost/edit_my_skin.html', context)

# def change_language(request, language):
#     '''更改语言'''
#     languages = settings.LANGUAGE_LIST
#     #判断语言是否是注册过的
#     if language in languages.keys():
#         request.session['language'] = language
#         request.session['django_language'] = language
#     #判断从哪里跳转过来的
#     if 'HTTP_REFERER' in request.META:
#         url = request.META['HTTP_REFERER']
#         #验证域名的合法性，是否是注册的域名，如果不是则跳转回首页
#         if not check_domian_legitimacy(url):
#             url = reverse('freightcost:index')
#     else:
#         #如果找不到就跳转回首页
#         url = reverse('freightcost:index')
#     return HttpResponseRedirect(url)
