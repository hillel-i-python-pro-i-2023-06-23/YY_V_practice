from django.urls import path

from apps.words import views

app_name = "words"

urlpatterns = [
    path("list/", views.GameWordsListView.as_view(), name="gamewords_list"),
#    path("create/", views.UserCreateView.as_view(), name="users_create"),
#    path("update/<int:pk>/", views.UserUpdateView.as_view(), name="users_update"),
#    path("delete/<int:pk>/", views.UserDeleteView.as_view(), name="users_delete"),
]
