from django.shortcuts import render, get_object_or_404
from hash_board.models import Post, Thread, Tag, ThreadTag

def index(request):
    return render(request, "hash_board/index.html")

def thread(request, thread_id):
    thread = get_object_or_404(Thread,pk=thread_id)

    # get the tags associated with this post
    if thread:
        thread_tags = ThreadTag.objects.filter(thread=thread)
        tags = [t.tag for t in thread_tags]
        print(tags)

    context_dict =  {
            'thread':thread,
            'tags':tags,
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
