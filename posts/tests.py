from django.test import TestCase
from .models import Post, Comment, Hashtag
from accounts.models import Account

class PostTestCase(TestCase):

    def setUp(self) -> None:
        self.account = Account.create_account(username='test', password = 'test', first_name='firsttest', last_name='lasttest', bio='testbio',birthdate='2000-2-2', avatar='default.png')
        ########
        # self.account.save()
        self.post = Post.objects.create(user_account= self.account, description="Test post", )
        return super().setUp()


    def test_is_any_like(self):
        self.assertFalse(self.post.is_any_like())
        
    def is_liked_by_user(self):
        self.assertFalse(self.post.is_liked_by_user(self.account))

    def test_like_post(self):  
        self.post.like_post(self.account)
        self.assertTrue(self.post.is_liked_by_user(self.account))
        
    def test_post_likes(self):
        self.post.like_post(self.account)
        likes = self.post.post_likes()
        self.assertEqual(likes.count(), 1)
       
    def test_post_media(self):
        self.assertEqual(self.post.post_media().count(), 0)
       
    def test_post_comments(self):
        self.assertEqual(self.post.post_comments().count(), 0)
       
    def test_post_hashtags(self):
        self.assertEqual(self.post.post_hashtags().count(), 0)
       
    def test__str__(self):
        self.assertEqual(str(self.post), "Test post")


class CommentTestCase(TestCase):

    def setUp(self) -> None:
        self.account = Account.create_account(username='test', password = 'test', first_name='firsttest', last_name='lasttest', bio='testbio',birthdate='2000-2-2', avatar='default.png')
        ########
        # self.account.save()
        self.post = Post.objects.create(user_account= self.account, description="Test post")
        self.comment = Comment.objects.create(user_post= self.post, author= self.account ,content='Comment') 
        return super().setUp()
      
    def test__str__(self):
        self.assertEqual(str(self.comment), self.comment.author.user.username) 
        
    def test_foreign_key(self):     
        self.assertEqual(self.comment.user_post, self.post)

    

class HashtagTestCase(TestCase):
     
     def setUp(self) -> None:
        self.account = Account.create_account(username='test', password = 'test', first_name='firsttest', last_name='lasttest', bio='testbio',birthdate='2000-2-2', avatar='default.png')
        ########
        # self.account.save()
        self.post = Post.objects.create(user_account= self.account, description="Test post")
        self.hashtag = Hashtag.objects.create(tag='test_tag') 
        self.hashtag.user_post.add(self.post)
        # self.hashtag.save()
        return super().setUp()

     def test_hashtag_posts(self):       
        self.assertEqual(Hashtag.hashtag_posts(self.hashtag.tag).count(), 1)
        self.assertEqual(Hashtag.hashtag_posts(self.hashtag.tag)[0], self.post)
        
