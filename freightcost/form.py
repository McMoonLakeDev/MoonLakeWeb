from django import forms
from .models import Entry


class EntryLowForm(forms.ModelForm):
    title_choice = (
        ("油费", "油费"),
        ("过路费", "过路费"),
        ("维修费用", "维修费用"),
        ("交通意外费用", "交通意外费用"),
        ("其他杂项", "其他杂项"),
    )
    title = forms.CharField(label="报销种类", widget=forms.widgets.Select(choices=title_choice))

    carNo = forms.CharField(
        label="车牌号",
        max_length=10,
        min_length=7,
        required=True,
        error_messages={
            'required': u'车牌号不能为空',
            'max_length': u'最少7个字符',
            'min_length': u'最多10个字符',
        },
        widget=forms.TextInput(attrs={'palceholder': u'输入现在车辆的车牌号'})
    )

    img = forms.FileField(label="报销图片",)

    text = forms.Textarea(
        attrs={'cols': 80},
    )

    amout = forms.DecimalField(
        label="报销金额",
        max_digits=9,
        decimal_places=2,
    )

    # wipeout = forms.BooleanField()

    class Meta:
        model = Entry
        fields = ['title', 'text', 'img', 'carNo', 'amout']
        # labels = {'title': '报销种类', 'text': '报销理由', 'img': '发票图片', 'carNo': '车牌号', 'amout': '报销金额'}
        # widgets = {'text': forms.Textarea(attrs={'cols': 80})}



class EntryHighForm(forms.ModelForm):
    title_choice = (
        ("油费", "油费"),
        ("过路费", "过路费"),
        ("维修费用", "维修费用"),
        ("交通意外费用", "交通意外费用"),
        ("其他杂项", "其他杂项"),
    )
    title = forms.CharField(label="报销种类", widget=forms.widgets.Select(choices=title_choice))

    carNo = forms.CharField(
        label="车牌号",
        max_length=10,
        min_length=7,
        required=True,
        error_messages={
            'required': u'车牌号不能为空',
            'max_length': u'最少7个字符',
            'min_length': u'最多10个字符',
        },
        widget=forms.TextInput(attrs={'palceholder': u'输入现在车辆的车牌号'})
    )

    img = forms.FileField(label="报销图片",)

    text = forms.Textarea(
        attrs={'cols': 80},
    )

    amout = forms.DecimalField(
        label="报销金额",
        max_digits=9,
        decimal_places=2,
    )

    # wipeout = forms.BooleanField()

    class Meta:
        model = Entry
        fields = "__all__"
        # labels = {'title': '报销种类', 'text': '报销理由', 'img': '发票图片', 'carNo': '车牌号', 'amout': '报销金额'}
        # widgets = {'text': forms.Textarea(attrs={'cols': 80})}