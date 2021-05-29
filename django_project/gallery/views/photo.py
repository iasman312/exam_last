from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from gallery.forms import PhotoForm
from gallery.models import Photo


class IndexView(ListView):
    template_name = 'photos/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ('-created_at',)


class PhotoView(DetailView):
    model = Photo
    template_name = 'photos/view.html'


class CreatePhotoView(CreateView):
    template_name = 'photos/create.html'
    form_class = PhotoForm
    model = Photo
    success_url = reverse_lazy('gallery:photo-list')

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.author = self.request.user
        photo.save()
        return super().form_valid(form)


class PhotoUpdateView(UpdateView):
    form_class = PhotoForm
    model = Photo
    template_name = 'photos/update.html'
    context_object_name = 'photo'

    def get_success_url(self):
        return reverse('gallery:photo-view', kwargs={'pk': self.kwargs.get('pk')})


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'photos/delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('gallery:photo-list')