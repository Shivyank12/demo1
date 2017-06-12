from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,get_object_or_404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.views.generic import View
from .models import Home,About
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'all_albums'

    def get_queryset(self):
        return  Home.objects.all()


class DetailView(generic.DetailView):
    model = Home
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    model = Home
    fields = ['artist','album_title','genre','album_logo']


class AlbumUpdate(UpdateView):
    model = Home
    fields = ['artist','album_title','genre','album_logo']


def delete_album(request, album_id):
        album = Album.objects.get(pk=album_id)
        album.delete()
        albums = Album.objects.filter(user=request.user)
        return render(request, 'music/index.html', {'albums': albums})


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)


        # clean {normalized} the data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user.set_password(password)
            user.save()
        # Return user object if credential are server

            user = authenticate(username =username, password=password)

            if user.is_active:
                login(request, user)
        return redirect('music:index')

        return render(request, self.template_name, {'form': form})


def delete_song(request,album_id,song_id):
    album = get_object_or_404(Album,pk=album_id)
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request,'music/detail.html',{'album': album})


def detail(request,album_id):
    if not request.user.is_authenticated():
        return render(request,'music/login.html')

    else:
        user = request.user
        album = get_object_or_404(Album,pk=album_id)
        return render(request,'music/detail.html',{'album': album,'user': user})
