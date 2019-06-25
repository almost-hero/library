from django.test import TestCase

from libmain.models import Book

class BookModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='django')

    def test_title_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEquals(max_length,100)

    def test_object_name_is_title(self):
        book = Book.objects.get(id=1)
        expected_object_name = '%s'% (book.title)
        self.assertEquals(expected_object_name,str(book))
