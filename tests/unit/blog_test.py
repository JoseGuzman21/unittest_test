from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_crete_blog(self):
        b = Blog('blog', 'jose')
        self.assertEqual('blog', b.title)
        self.assertEqual('jose', b.author)
    
    def test_b2(self):
        b2 = Blog('My Day', 'Jose')
        b2.posts = [1, 2]
        self.assertEqual(b2.test_b2(), 'My Day by Jose tiene 2 posts')
