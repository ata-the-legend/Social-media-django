from django.test import TestCase
from .models import Post
from accounts.models import Account

class PostTestCase(TestCase):

    def setUp(self) -> None:
        self.account = Account.create_account(username='test', password = 'test', first_name='firsttest', last_name='lasttest', bio='testbio',birthdate='2000-2-2', avatar='default.png')
        print(self.account)
        print(self.account.avatar)
        self.post = Post.objects.create(user_account= self.account, description="Test post", )
        return super().setUp()


    def test_is_any_like(self):
        post = Post.objects.create(description="Test post")
        self.assertFalse(post.is_any_like())
        
    def test_like_post(self):
        post = Post.objects.create(description="Test post")
        account = Account.objects.create()  
        post.like_post(account)
        self.assertTrue(post.is_liked_by_user(account))
        
    def test_post_likes(self):
       ...
       
    def test_post_media(self):
        self.assertEqual(post.post_media().count(), 0)
       
    def test_post_comments(self):
        self.assertEqual(post.post_comments().count(), 0)
       
    def test_post_hashtags(self):
        self.assertEqual(post.post_hashtags().count(), 0)
       
    def test__str__(self):
        post = Post.objects.create(description="Test")
        self.assertEqual(str(post), "Test")


class CommentTestCase(TestCase):
      
    def test__str__(self):
        comment = Comment.objects.create(content='Comment')       
        self.assertEqual(str(comment), comment.author.user.username) 
        
    def test_foreign_key(self):   
        post = Post.objects.create()   
        comment = Comment.objects.create(post=post)  
        self.assertEqual(comment.post, post)

    

class HashtagTestCase(TestCase):

     def test_hashtag_posts(self):
        hashtag = Hashtag.objects.create(tag="test")   
        post = Post.objects.create()       
        hashtag.user_post.add(post)
        self.assertEqual(hashtag.hashtag_posts().count(), 1)
