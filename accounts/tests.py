from django.test import TestCase
from .models import Account
from django.contrib.auth.models import User

class AccountTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='john', password='password')

    def test_str(self):
        account = Account.objects.create(user=self.user)
        self.assertEqual(str(account), 'john')
    
    def test_user_posts(self):
        account = Account.objects.create(user=self.user)
        self.assertEqual(account.user_posts.count(), 0)
        
    def test_create_account(self):
        account = Account.create_account('jane', 'password', '', '',  '1990-01-01')
        self.assertTrue(User.objects.filter(username='jane').exists())
        
    def test_user_followers(self):
        account1 = Account.objects.create(user=self.user)
        account2 = Account.objects.create(user=User.objects.create_user(username='jane')) 
        account1.follow(account2)
        self.assertEqual(account1.user_followers().count(), 0)
        self.assertEqual(account2.user_followers().count(), 1)
