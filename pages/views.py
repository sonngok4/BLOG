from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *

from .models import *
from django.urls import reverse_lazy


def error404(request, exception):
    return HttpResponse("<h1>Page not found</h1>")


def error500(request):
    return HttpResponse("""<h1>Internal server error</h1>""")


class HomePageView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "all_posts_list"


class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"


class BlogCreateView(CreateView):  # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "content", "image", "audio", "video"]


class BlogUpdateView(UpdateView):  # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "content", "image", "audio", "video"]


class BlogDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


class AboutPageView(TemplateView):
    template_name = "about.html"


class ErrorPageView(TemplateView):
    template_name = "error.html"

    def handle_no_permission(self):
        return render(self.request, self.template_name)


class SignupView(TemplateView):
    template_name = "signup.html"

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST)
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect("/")
        return render(request, self.template_name, {"form": form})


class LoginView(TemplateView):
    template_name = "registration/login.html"

    def post(self, request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Successfully Logged In")
                return HttpResponseRedirect("/")
            else:
                messages.error(request, "Invalid Credentials")
            return render(request, self.template_name)
        return render(request, self.template_name)


class LogoutView(TemplateView):
    def post(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, "Successfully logged out")
        return HttpResponseRedirect("/")
