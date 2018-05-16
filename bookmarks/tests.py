from django.db.utils import IntegrityError
from django.test import TestCase
from .models import Bookmark

# Create your tests here.
class BookmarkTestCase(TestCase):
    def setUp(self):
        Bookmark.objects.create(name='This is a bookmark',
                                url='http://www.example.com')
        Bookmark.objects.create(name='A bookmark with a note!',
                                notes='This bookmark is noteworthy',
                                url='http://www.noteworthy.com')

    def test_retrieving_all_bookmarks(self):
        """Test that there are the expected number of bookmarks."""
        bookmarks = Bookmark.objects.all()
        self.assertEqual(len(bookmarks), 2)

    def test_retrieving_bookmarks_by_name(self):
        bookmark = Bookmark.objects.get(name='This is a bookmark')
        self.assertEqual(bookmark.name, 'This is a bookmark')
        self.assertEqual(bookmark.notes, '')
        self.assertEqual(bookmark.url, 'http://www.example.com')

    def test_retrieving_bookmarks_by_url(self):
        bookmark = Bookmark.objects.get(url='http://www.noteworthy.com')
        self.assertEqual(bookmark.name, 'A bookmark with a note!')
        self.assertEqual(bookmark.notes, 'This bookmark is noteworthy')
        self.assertEqual(bookmark.url, 'http://www.noteworthy.com')

    def test_dupe_urls(self):
        """Ensure database enforces unique urls."""
        with self.assertRaises(IntegrityError) as context:
            Bookmark.objects.create(name='This is another bookmark, really!',
                                    url='http://www.example.com')
        self.assertEqual('UNIQUE constraint failed: bookmarks_bookmark.url', str(context.exception))
