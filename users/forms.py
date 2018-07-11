from django.contrib.auth.forms import UserCreationForm, UsernameField
from django import forms
from .models import User


class RegisterUserForm(UserCreationForm):
    nickname = forms.CharField(
        label="昵称",
        widget=forms.TextInput,
        strip=False,
        help_text="在月色之湖游玩时将显示此昵称",
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
            userinfo.nickname = self.cleaned_data['nickname']
            userinfo.save()
        return user

    def clean_nickname(self):
        nickname = self.cleaned_data.get("nickname")
        userinfo = User.objects.filter(nickname=nickname)

        if userinfo:
            raise forms.ValidationError(
                "用户已经注册这个昵称，请勿重复注册",
                code='nickname_error',
            )
        else:
            return nickname
