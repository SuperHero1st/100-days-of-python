class Post:
    def __init__(self, blog_post) -> None:
        self.title = blog_post["title"]
        self.subtitle = blog_post["subtitle"]
        self.id = blog_post["id"]
        self.body = blog_post["body"]
    pass