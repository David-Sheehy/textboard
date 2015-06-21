from django.db import models

class Thread(models.Model):
    """
    A particular thread. It's actually a collection of posts and Tags.
    """
    pass

class Post(models.Model):
    contents = models.TextField(default="")
    number = models.IntegerField()
    pass

class Tag(models.Model):
    tag = contents.TextField(max_lenght=20)
    pass
