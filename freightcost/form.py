from django import forms
from .models import Skin

class SkinForm(forms.ModelForm):
    fileinput = forms.ImageField()

    class Meta:
        model = Skin
        fields = "__all__"

