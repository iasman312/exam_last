from django import forms

from gallery.models import Photo, Album


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'signature', 'album', 'type',)


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'description', 'type')
