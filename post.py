class Post:
    # es el main
    def __init__(self, title, content, fecha):
        self.title = title
        self.content = content
        self.fecha = fecha

    def create_post(self, title, content, fecha):
        return {'title': self.title, 'content': self.content, 'fecha': self.fecha,}

