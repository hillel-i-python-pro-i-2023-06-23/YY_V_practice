from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.users.models import Gamer


class UsersListView(ListView):
    model = Gamer


class UserCreateView(CreateView):
    model = Gamer
    fields = (
        "name",
        "email",
        "password",
    )

    success_url = reverse_lazy("users:user_list")


class UserUpdateView(UpdateView):
    model = Gamer
    fields = (
        "name",
        "email",
    )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["is_update"] = True
        return context

    success_url = reverse_lazy("users:user_list")


class UserDeleteView(DeleteView):
    model = Gamer
    success_url = reverse_lazy("users:user_list")
