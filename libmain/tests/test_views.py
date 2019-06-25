from django.test import TestCase

from django.contrib.auth.models import User
from django.urls import reverse

class UsersListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_users = 13
        for user_num in range(number_of_users):
            User.objects.create(username='admin%s' % user_num, password = 'admin%s' % user_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'libmain/users_list.html')
