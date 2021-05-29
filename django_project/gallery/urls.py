from django.urls import path

from gallery.views import (
    IndexView,
    # ArticleView,
    # CreateArticleView,
    # ArticleUpdateView,
    # ArticleCommentCreate,
    # ArticleDeleteView,
    # LikeView,
    # LikeCommentView
)


app_name = 'gallery'

urlpatterns = [
    path('', IndexView.as_view(), name='photo-list'),
    # path('add/', CreateArticleView.as_view(), name='add'),
    # path('<int:pk>/', ArticleView.as_view(), name='view'),
    # path('<int:pk>/update', ArticleUpdateView.as_view(), name='update'),
    # path('<int:pk>/delete', ArticleDeleteView.as_view(), name='delete'),
    # path('<int:pk>/comments/add/', ArticleCommentCreate.as_view(), name='comment-create'),
    # path('like/<int:pk>/', LikeView.as_view(), name='like_article'),
    # path('like_comment/<int:pk>/', LikeCommentView.as_view(), name='like_comment'),
]