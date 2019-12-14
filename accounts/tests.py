from django.test import TestCase

# Create your tests here.
class AccountsUrlTest(TestCase):
    def test_status_code_of_signup(self):
       response = self.client.get('/accounts/login')
       self.assertEqual(response.status_code, 301)
