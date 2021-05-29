from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from gallery.forms import PhotoForm, AlbumForm
from gallery.models import Photo, Album


class AlbumView(DetailView):
    model = Album
    template_name = 'albums/view.html'


class CreateAlbumView(CreateView):
    template_name = 'albums/create.html'
    form_class = AlbumForm
    model = Album
    success_url = reverse_lazy('gallery:album-list')

    def form_valid(self, form):
        album = form.save(commit=False)
        album.author = self.request.user
        album.save()
        return redirect(self.get_success_url())


class AlbumUpdateView(PermissionRequiredMixin, UpdateView):
    form_class = AlbumForm
    model = Album
    template_name = 'albums/update.html'
    context_object_name = 'album'
    permission_required = 'gallery.change_album'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()


    def get_success_url(self):
        return reverse('gallery:album-view', kwargs={'pk': self.kwargs.get('pk')})


class AlbumDeleteView(PermissionRequiredMixin, DeleteView):
    model = Album
    template_name = 'albums/delete.html'
    context_object_name = 'album'
    success_url = reverse_lazy('gallery:album-list')
    permission_required = 'gallery.delete_album'

    def has_permission(self):
        return self.get_object().author == self.request.user or super().has_permission()
