from django.shortcuts import render

def index(request):
    return render(request, "hash_board/index.html")

def thread(request, thread_id):
    context_dict =  {
            'thread_id':thread_id,
        }

    return render(request, "hash_board/thread.html", context_dict)

def  tag(request, tag_id):
    context_dict = {
            'tag_id':tag_id,

        }
    return render(request, "hash_board/tag.html",context_dict)
