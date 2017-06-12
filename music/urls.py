from django.conf.urls import url

from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /music/album/add/
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),

    url(r'^(?P<album_id>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album_update'),

    # /music/album/delete/2/
   url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),

]

