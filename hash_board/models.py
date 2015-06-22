from django.db import models

class Thread(models.Model):
    """
    A particular thread. It's actually a collection of posts and Tags.
    """
    number = models.IntegerField(primary_key=True)
    title = models.TextField(default="default title", max_length=42)

    def __str__(self):
        return "{}".format(self.number)
    # The tags

class Post(models.Model):
    contents = models.TextField(default="")
    number = models.IntegerField(primary_key=True)

    thread = models.ForeignKey(Thread)
    def __str__(self):
        return "{}".format(self.contents)

class Tag(models.Model):
    name = models.TextField(primary_key=True,max_length=20)

    def __str__(self):
        return "{}".format(self.name)

class ThreadTag(models.Model):
    """
    A mapping class that handles the many to many relationship
    """
    thread = models.ForeignKey(Thread, default=None)
    tag = models.ForeignKey(Tag, default=None)

    def __str__(self):
        return "thread:{}, tag{}".format(self.thread,self.tag)
