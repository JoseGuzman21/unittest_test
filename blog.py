class Blog:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return 'Test by Test Author (0 posts)'

    def test_b2(self):
        if len(self.posts) < 2:
            return self.title + ' by ' + self.author + ' tiene ' + str(len(self.posts)) + ' post'
        return self.title + ' by ' + self.author + ' tiene ' + str(len(self.posts)) + ' posts'
