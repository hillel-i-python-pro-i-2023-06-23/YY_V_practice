from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.words.models import GameWords


class GameWordsListView(ListView):
    model = GameWords


#

class GameWordsUpdateView(UpdateView):
    model = GameWords
    fields = (
        "name_of_gamer",
        "word",
    )

    success_url = reverse_lazy("words:gamewords_list")

# class UserDeleteView(DeleteView):
#    model = Gamer
#    success_url = reverse_lazy("users:user_list")
