from django.test import TestCase
from .models import Account
from posts.models import Post
from relations.models import UserFollow
from django.contrib.auth.models import User

class AccountTestCase(TestCase):

    def setUp(self):
        self.account = Account.create_account(username='test', password = 'test', first_name='firsttest', last_name='lasttest', bio='testbio',birthdate='2000-2-2')
        print(self.account.avatar.url)
        self.post = Post.objects.create(user_account= self.account, description="Test post", )
        self.account2 = Account.create_account(username='test2', password = 'test', first_name='firsttest', last_name='lasttest', bio='testbio',birthdate='2000-2-2', avatar='default.png')
        return super().setUp()

    def test_str(self):
        self.assertEqual(self.account.user.username, 'test')
    
    def test_user_posts(self):
        self.assertEqual(self.account.user_posts.count(), 1)
        
    def test_create_account(self):
        self.assertTrue(User.objects.filter(username='test').exists())

    def test_follow(self):
        self.account.follow(self.account2)
        self.assertTrue(UserFollow.objects.filter(follower= self.account, followee= self.account2).exists())

    def test_unfollow(self):
        self.account.follow(self.account2)
        self.account.unfollow(self.account2)
        self.assertFalse(UserFollow.objects.filter(follower= self.account, followee= self.account2).exists())
        
    def test_user_followers(self):
        self.account.follow(self.account2)
        self.assertEqual(self.account.user_followers().count(), 0)
        self.assertEqual(self.account2.user_followers().count(), 1)

    def test_user_followees(self):
        self.account.follow(self.account2)
        self.assertEqual(self.account.user_followees().count(), 1)
        self.assertEqual(self.account2.user_followees().count(), 0)

    def test_is_followed(self):
        self.account.follow(self.account2)
        self.assertTrue(self.account.is_followed(self.account2))

    def test_archive(self):
        self.account.archive()
        self.assertFalse(self.account.is_active)
        self.assertFalse(self.account.user.is_active)

    def test_restore(self):
        self.account.archive()
        self.account.restore()
        self.assertTrue(self.account.is_active)
        self.assertTrue(self.account.user.is_active)
