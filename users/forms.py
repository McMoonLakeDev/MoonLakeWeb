from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from .models import User


class RegisterUserForm(UserCreationForm):
    realname = forms.CharField(
        label="真实姓名",
        widget=forms.TextInput,
        strip=False,
        help_text="输入司机或会计的姓名",
    )

    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            userinfo = User.objects.get(username=self.cleaned_data['username'])
            userinfo.realname = self.cleaned_data['realname']
            userinfo.save()
        return user

    def clean_realname(self):
        realname = self.cleaned_data.get("realname")
        userinfo = User.objects.filter(realname=realname)
        if userinfo:
            raise forms.ValidationError(
                "用户已经注册这个名字，请勿重复注册",
                code='realname_error',
            )
        else:
            return realname
