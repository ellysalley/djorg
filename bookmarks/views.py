from django.shortcuts import render
from .forms import BookmarkForm
from .models import Bookmark, PersonalBookmark
from django.http import HttpResponseRedirect

def index(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            pass
    context = {}
    context['bookmarks'] = Bookmark.objects.exclude(
        id__in=PersonalBookmark.objects.values_list('id'))
    if request.user.is_anonymous:
        context['personal_bookmarks'] = PersonalBookmark.objects.none()
    else:
        context['personal_bookmarks'] = PersonalBookmark.objects.filter(
            user=request.user)
    context['form'] = BookmarkForm()
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
            