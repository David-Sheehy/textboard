from django.shortcuts import render, get_object_or_404
from hash_board.models import Post, Thread, Tag, ThreadTag

def index(request):
    # get the top few tags
    # Should be replaced by the most popular
    tags = Tag.objects.all()[:10]
    threads = Thread.objects.all()[:10]

    context_dict = {
        'tags':tags,
        'threads':threads,
    }

    return render(request, "hash_board/index.html", context_dict)

def thread(request, thread_number):
    thread = get_object_or_404(Thread,pk=thread_number)

    # get the tags associated with this post
    thread_tags = ThreadTag.objects.filter(thread=thread)
    tags = [t.tag for t in thread_tags]
    posts = Post.objects.filter(thread=thread)


    context_dict =  {
            'thread':thread,
            'tags':tags,
            'posts':posts,
        }

    return render(request, "hash_board/thread.html", context_dict)

def  tag(request, tag_name):
    tag = get_object_or_404(Tag,pk=tag_name)

    if tag:
        thread_tags = ThreadTag.objects.filter(tag=tag)
        threads = [t.thread for t in thread_tags]

    context_dict = {
            'tag':tag,
            'threads':threads,
        }
    return render(request, "hash_board/tag.html",context_dict)
