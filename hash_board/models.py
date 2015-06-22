from django.db import models

class Thread(models.Model):
    """
    A particular thread. It's actually a collection of posts and Tags.
    """
    number = models.IntegerField(primary_key=True)
    title = models.TextField(default="default title", max_length=42)

    def __str__(self):
        return "{}".format(self.number)
    # The posts
    # The tags
    pass

class Post(models.Model):
    contents = models.TextField(default="")
    number = models.IntegerField(primary_key=True)

    def __str__(self):
        return "{}".format(self.number)
    pass

class Tag(models.Model):
    tag = models.TextField(primary_key=True,max_length=20)

    def __str__(self):
        return "{}".format(self.tag)

    pass
