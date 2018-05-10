from django.shortcuts import render
from .forms import BookmarkForm
from .models import Bookmark
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
    context = { 'bookmarks': Bookmark.objects.all(), 
                'form': BookmarkForm(), 
                'action': 'Create', 
                'button': 'Create',
                }
    return render(request, 'bookmarks/index.html', context)

def update(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bookmarks')
    context = { 'bookmarks': Bookmark.objects.all(),
                'form': BookmarkForm(),
                'action': 'Update',
                'button': 'Update',
                }
    return render(request, 'bookmarks/index.html', context)

def delete(request, bookmark_id):
    bookmark = Bookmark.objects.get(pk=bookmark_id)
    if bookmark:
        bookmark.delete()
        return HttpResponseRedirect('/bookmarks')
            