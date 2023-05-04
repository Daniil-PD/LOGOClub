
from django.shortcuts import render
from .models import Post


# Create your views here.
def main_render(request):
    return render(request, "main/main.html")


def aboutus_render(request):
    return render(request, "main/aboutus.html")


def contacts_render(request):
    return render(request, "main/contacts.html")


def logosad_render(request):
    return render(request, "main/logosad.html")


def serveses_render(request):
    return render(request, "main/serveses.html")


def states_render(request):
    posts = Post.objects.order_by('-id')[:9]
    # В словаре context отправляем информацию в шаблон
    MAX_LEN_POST_PREVIEW = 80
    for post in posts:
        if len(post.text) > MAX_LEN_POST_PREVIEW:
            post.text = post.text[:MAX_LEN_POST_PREVIEW] + "..."
    context = {
        'posts': posts,

    }
    return render(request, 'main/states.html', context)
