from django.shortcuts import render
from .models import Entry
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .form import EntryLowForm,EntryHighForm
from django.conf import settings


# Create your views here.
def index(request):
    '''学习笔记的主页'''
    return render(request, 'freightcost/index.html')


@login_required
def entries(request):
    '''显示所有的主题'''
    entries = Entry.objects.filter(owner=request.user, wipeout=False).order_by('-date_added')
    context = {'entries': entries}
    return render(request, 'freightcost/entries.html', context)


@login_required
def entry(request, entry_id):
    '''显示单个主题及所有的条目'''
    entry = Entry.objects.get(bxno=entry_id)
    # 确认请求的主题属于当前用户
    if entry.owner != request.user:
        raise Http404
    context = {'entry': entry}
    return render(request, 'freightcost/entry.html', context)


# @login_required
# def new_topic(request):
#     '''添加新主题'''
#     if request.method != 'POST':
#         # 未提交数据：创建一个新表单
#         translation.activate(request.session.get('django_language',translation.get_language()))
#         form = TopicForm()
#     else:
#         # POST提交的数据，对数据进行处理
#         form = TopicForm(request.POST)
#         if form.is_valid():
#             new_topic = form.save(commit=False)
#             new_topic.owner = request.user
#             new_topic.save()
#             return HttpResponseRedirect(reverse('freightcost:topics'))
#
#     context = {'form': form}
#     return render(request, 'freightcost/new_topic.html', context)


@login_required
def new_entry(request):
    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryLowForm()
    else:
        form = EntryLowForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.owner = request.user

            new_entry.save()
            return HttpResponseRedirect(reverse('freightcost:entries'))
    context = {'form': form}
    return render(request, 'freightcost/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    '''
    编辑既有条目
    :param request:
    :param entry_id:
    :return:
    '''
    entry = Entry.objects.get(bxno=entry_id)

    if entry.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # 初次请求建立表单
        form = EntryLowForm(instance=entry)
    else:
        # POST提交数据就对其进行处理
        form = EntryLowForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('freightcost:entry',
                                                args=[entry.bxno]))

    context = {'entry': entry, 'form': form}
    return render(request, 'freightcost/edit_entry.html', context)

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
