from django.test import TestCase
from myapp.models import Post, Comment
import datetime

# Create your tests here.
class TestPosts(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title = "Hello",
            likes = 50,
            date = datetime.datetime.now()
        )

        self.comment1 = Comment.objects.create(
            content = "Hi",
            post = self.post
        )
    
    def test_delete_post(self):
        self.post.delete()
        self.assertEqual(len(Comment.objects.all()), 0)
    
    def test_check_comments(self):
        self.assertEqual(len(self.post.comments.all()), 1)