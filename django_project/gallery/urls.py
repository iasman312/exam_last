from django.urls import path

from gallery.views import (
    IndexView,
    PhotoView,
    CreatePhotoView,
    PhotoUpdateView,
    PhotoDeleteView,
    CreateAlbumView,
    AlbumView,
    AlbumUpdateView,
    AlbumDeleteView,
)


app_name = 'gallery'

urlpatterns = [
    path('', IndexView.as_view(), name='photo-list'),
    path('image/add/', CreatePhotoView.as_view(), name='photo-add'),
    path('image/<int:pk>/', PhotoView.as_view(), name='photo-view'),
    path('image/<int:pk>/update/', PhotoUpdateView.as_view(), name='photo-update'),
    path('image/<int:pk>/delete/', PhotoDeleteView.as_view(), name='photo-delete'),
    path('add/', CreateAlbumView.as_view(), name='album-add'),
    path('<int:pk>/', AlbumView.as_view(), name='album-view'),
    path('<int:pk>/update/', AlbumUpdateView.as_view(), name='album-update'),
    path('<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
]