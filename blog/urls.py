from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("", views.post_list, name="home"),
    path("post/<int:pk>/", views.post_detail, name="detail"),
]