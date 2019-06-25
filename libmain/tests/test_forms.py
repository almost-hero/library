from django.test import TestCase
import datetime

from libmain.forms import *

class AddUserFormTest(TestCase):

    def test_add_user_form_username_label(self):
        form = AddUser()
        self.assertTrue(form.fields['username'].label == None or form.fields['username'].label == 'Username')

    def test_add_user_form_pasword_label(self):
        form = AddUser()
        self.assertTrue(form.fields['password'].label == None or form.fields['password'].label == 'Password')

class AddBookFormTest(TestCase):

    def test_add_book_form_title_label(self):
        form = AddBook()
        self.assertTrue(form.fields['title'].label == None or form.fields['title'].label == 'Title')

    def test_add_book_form_slug_label(self):
        form = AddBook()
        self.assertTrue(form.fields['slug'].label == None or form.fields['slug'].label == 'Slug')

    def test_add_book_form_author_label(self):
        form = AddBook()
        self.assertTrue(form.fields['author'].label == None or form.fields['author'].label == 'Author')

    def test_add_book_form_date_label(self):
        form = AddBook()
        self.assertTrue(form.fields['date'].label == None or form.fields['date'].label == 'Date')

    def test_add_book_form_date_more_then_now(self):
        date = str(datetime.date.today().year)
        form_data = {'date':date}
        form = AddBook(data=form_data)
        self.assertFalse(form.is_valid())
