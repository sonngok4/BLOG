from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    ErrorPageView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView,
)


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("error/", ErrorPageView.as_view(), name="error"),  # For testing error handling
    path(
        "<int:pk>/", BlogDetailView.as_view(), name="post_detail"
    ),  # Use the same view for both lists and details
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),  # new
]
