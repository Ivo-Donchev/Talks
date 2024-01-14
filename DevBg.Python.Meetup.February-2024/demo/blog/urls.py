from django.urls import path
from .apis import ArticleDetaiApiView, CommentListApiView


urlpatterns = [
    path("articles/<int:pk>/", ArticleDetaiApiView.as_view(), name="article-detail"),
    path(
        "articles/<int:pk>/comments/",
        CommentListApiView.as_view(),
        name="article-comments",
    ),
]
