from django import forms

from apps.words.models import GameWords


class GameWordsForm(forms.ModelForm):
    class Meta:
        model = GameWords
