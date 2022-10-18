from django.shortcuts import render

# def post_list(request):
#     return render(request, 'posts/post_list.html', {})


def PostListView(ListView):
    return render(ListView, 'post_list.html', {} )