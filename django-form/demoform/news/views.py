from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .forms import PostForm, SendEmail


# Create your views here.
# Function Based view
def add_post(request):
    a = PostForm()
    return render(request, 'news/add_news.html', {'f': a})


def save_news(request):
    if request.method == "POST":
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Saved!")
        else:
            return HttpResponse("Not validated")
    else:
        return HttpResponse("Not post request!")


def send_email(request):
    g = SendEmail()
    return render(request, "news/send_email.html", {"f": g})


def show_email(request):
    if request.method == "POST":
        g = SendEmail(request.POST)
        if g.is_valid():
            # title = g.cleaned_data['title']
            # email = g.cleaned_data['email']
            # content = g.cleaned_data['content']
            # cc = g.cleaned_data['cc']
            # info = {"title": title, "email": email, "content": content, "cc": cc}
            return render(request, 'news/email_info.html', {"info": g})
        else:
            return HttpResponse("Not validated")
    else:
        return HttpResponse("Not post request!")


# Class Based View
class Index(View):
    def get(self, request):
        return HttpResponse("Hello World")


class AddPost(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f': a})

    def post(self, request):
        g = PostForm(request.POST)
        if g.is_valid():
            g.save()
            return HttpResponse("Saved!")
        else:
            return HttpResponse("Not validated")


class Send_Email(View):
    def get(self, request):
        g = SendEmail()
        return render(request, 'news/send_email.html', {'f': g})


class ShowEmail(View):
    def post(self, request):
        g = SendEmail(request.POST)
        if g.is_valid():
            return render(request, 'news/email_info.html', {"info": g})
        else:
            return HttpResponse("Not validated!")
