from unittest import TestCase
from post import Post

class PostTest(TestCase):
    def test_post(self):
        p = Post('Test', 'Test Content', '04-10-2020')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)
    
    def test_create_post(self):
        p1 = Post('Post', 'Post description', '04-10-2020')
        json_test = {'title': 'Post', 'content': 'Post description', 'fecha': '04-10-2020'}
        self.assertDictEqual(json_test, p1.create_post(p1.title, p1.content, p1.fecha))

