from django import forms

from apps.users.models import Gamer


class GameWordsForm(forms.ModelForm):
    class Meta:
        model = Gamer
        widgets = {
            'password': forms.PasswordInput(),
        }
