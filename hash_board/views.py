from django.shortcuts import render, get_object_or_404
from hash_board.models import Post, Thread, Tag

def index(request):
    return render(request, "hash_board/index.html")

def thread(request, thread_id):
    thread = get_object_or_404(Thread,pk=thread_id)
    context_dict =  {
            'thread':thread
        }

    return render(request, "hash_board/thread.html", context_dict)

def  tag(request, tag_name):
    tag = get_object_or_404(Tag,pk=tag_name)
    context_dict = {
            'tag':tag,
        }
    return render(request, "hash_board/tag.html",context_dict)
